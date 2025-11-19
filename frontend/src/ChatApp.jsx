import { useState, useEffect, useRef } from 'react'
import JSZip from 'jszip'
import './ChatApp.css'
import PreviewV2 from './components/PreviewV2'
import FileTree from './components/FileTree'
import PaymentGatewaySelector from './components/PaymentGatewaySelector'
import {
  generateThreadId,
  loadChatThread,
  autoSaveThread,
  getThreadsList,
  deleteChatThread,
  setCurrentThread,
  getCurrentThread
} from './utils/chatStorage'

function ChatApp() {
  // Thread management
  const [currentThreadId, setCurrentThreadIdState] = useState(null)
  const [threadsList, setThreadsList] = useState([])
  const [showThreadsList, setShowThreadsList] = useState(false)

  // Project state
  const [projectFiles, setProjectFiles] = useState({})
  const [projectName, setProjectName] = useState('')
  const [projectType, setProjectType] = useState('')
  const [paymentGateway, setPaymentGateway] = useState(null)
  const [projectSessionId, setProjectSessionId] = useState(null)
  const [liveUrl, setLiveUrl] = useState(null)

  // Chat state
  const [messages, setMessages] = useState([
    {
      type: 'assistant',
      content: '👋 Ready to build something extraordinary? Describe your dream website.',
      timestamp: new Date()
    }
  ])
  const [inputValue, setInputValue] = useState('')
  const [isGenerating, setIsGenerating] = useState(false)

  // UI state
  const [selectedFile, setSelectedFile] = useState(null)
  const [showPreview, setShowPreview] = useState(false)

  // Payment gateway question
  const [showPaymentSelector, setShowPaymentSelector] = useState(false)
  const [paymentQuestion, setPaymentQuestion] = useState('')
  const [paymentOptions, setPaymentOptions] = useState([])

  // WebSocket
  const [status, setStatus] = useState('disconnected')
  const wsRef = useRef(null)
  const chatEndRef = useRef(null)

  // Initialize
  useEffect(() => {
    const savedThreadId = getCurrentThread()
    if (savedThreadId) {
      const threadData = loadChatThread(savedThreadId)
      if (threadData) {
        setCurrentThreadIdState(savedThreadId)
        setMessages(threadData.messages || [])
        setProjectFiles(threadData.projectFiles || {})
        setProjectName(threadData.projectName || '')
        setProjectType(threadData.projectType || '')
        setPaymentGateway(threadData.paymentGateway || null)
        setProjectSessionId(threadData.projectSessionId || null)
        if (threadData.projectFiles && Object.keys(threadData.projectFiles).length > 0) {
          setShowPreview(true)
          const firstFile = Object.keys(threadData.projectFiles)[0]
          if (firstFile) setSelectedFile(firstFile)
        }
      } else {
        const newThreadId = generateThreadId()
        setCurrentThreadIdState(newThreadId)
        setCurrentThread(newThreadId)
      }
    } else {
      const newThreadId = generateThreadId()
      setCurrentThreadIdState(newThreadId)
      setCurrentThread(newThreadId)
    }
    setThreadsList(getThreadsList())
  }, [])

  // Auto-save
  useEffect(() => {
    if (currentThreadId && messages.length > 0) {
      autoSaveThread(currentThreadId, messages, {
        projectFiles, projectName, projectType, paymentGateway, projectSessionId
      })
      setThreadsList(getThreadsList())
    }
  }, [messages, projectFiles, projectName, projectType, paymentGateway, projectSessionId, currentThreadId])

  // Scroll to bottom
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, isGenerating])

  // WebSocket
  useEffect(() => {
    let reconnectAttempts = 0
    const maxReconnectAttempts = 5
    let reconnectTimeout = null

    const connectWebSocket = () => {
      if (reconnectAttempts >= maxReconnectAttempts) {
        console.error('Max reconnection attempts reached. Please refresh the page.')
        setStatus('error')
        return
      }

      const ws = new WebSocket('ws://localhost:8000/ws')

      ws.onopen = () => {
        console.log('✅ WebSocket connected')
        setStatus('connected')
        reconnectAttempts = 0 // Reset on successful connection
      }

      ws.onmessage = (event) => {
        const data = JSON.parse(event.data)
        handleWebSocketMessage(data)
      }

      ws.onerror = (error) => {
        console.error('WebSocket error:', error)
        setStatus('error')
      }

      ws.onclose = (event) => {
        console.log('WebSocket disconnected:', event.code, event.reason)
        setStatus('disconnected')
        reconnectAttempts++

        // Only reconnect if not max attempts and not a clean close
        if (reconnectAttempts < maxReconnectAttempts && event.code !== 1000) {
          const delay = Math.min(1000 * Math.pow(2, reconnectAttempts), 10000)
          console.log(`Reconnecting in ${delay/1000}s... (attempt ${reconnectAttempts}/${maxReconnectAttempts})`)
          reconnectTimeout = setTimeout(connectWebSocket, delay)
        }
      }

      wsRef.current = ws
    }

    connectWebSocket()

    return () => {
      if (reconnectTimeout) clearTimeout(reconnectTimeout)
      if (wsRef.current) {
        wsRef.current.close(1000, 'Component unmounting')
      }
    }
  }, [])

  const addMessage = (type, content, data = null) => {
    setMessages(prev => [...prev, { type, content, data, timestamp: new Date() }])
  }

  const handleWebSocketMessage = (data) => {
    switch (data.type) {
      case 'status':
        addMessage('system', data.message)
        break
      case 'question':
        setPaymentQuestion(data.question)
        setPaymentOptions(data.options)
        setShowPaymentSelector(true)
        break
      case 'project':
        setIsGenerating(false)
        setProjectFiles(data.files)
        setProjectName(data.projectName)
        setProjectType(data.projectType)
        setPaymentGateway(data.paymentGateway)
        setProjectSessionId(data.sessionId)
        setLiveUrl(data.liveUrl)
        const firstFile = Object.keys(data.files)[0]
        if (firstFile) setSelectedFile(firstFile)
        setShowPreview(true)
        addMessage('assistant', `🚀 Project "${data.projectName}" is ready!`, {
          type: 'project',
          fileCount: Object.keys(data.files).length,
          projectType: data.projectType,
          projectName: data.projectName,
          liveUrl: data.liveUrl
        })
        break
      case 'file_updated':
        setProjectFiles(prev => ({ ...prev, [data.filePath]: data.content }))
        addMessage('assistant', data.fixed ? `✅ Fixed error in ${data.filePath}` : `✅ Updated ${data.filePath}`)
        break
      case 'error':
        setIsGenerating(false)
        addMessage('system', `❌ Error: ${data.message}`)
        break
      default: break
    }
  }

  const createNewThread = () => {
    const newThreadId = generateThreadId()
    setCurrentThreadIdState(newThreadId)
    setCurrentThread(newThreadId)
    setMessages([{ type: 'assistant', content: '👋 Ready to build something extraordinary?', timestamp: new Date() }])
    setProjectFiles({})
    setProjectName('')
    setProjectType('')
    setPaymentGateway(null)
    setProjectSessionId(null)
    setShowPreview(false)
    setSelectedFile(null)
    setShowThreadsList(false)
  }

  const loadThread = (threadId) => {
    const threadData = loadChatThread(threadId)
    if (threadData) {
      setCurrentThreadIdState(threadId)
      setCurrentThread(threadId)
      setMessages(threadData.messages || [])
      setProjectFiles(threadData.projectFiles || {})
      setProjectName(threadData.projectName || '')
      setProjectType(threadData.projectType || '')
      setPaymentGateway(threadData.paymentGateway || null)
      setProjectSessionId(threadData.projectSessionId || null)
      if (threadData.projectFiles && Object.keys(threadData.projectFiles).length > 0) {
        setShowPreview(true)
        const firstFile = Object.keys(threadData.projectFiles)[0]
        if (firstFile) setSelectedFile(firstFile)
      } else {
        setShowPreview(false)
      }
      setShowThreadsList(false)
    }
  }

  const deleteThread = (threadId) => {
    if (confirm('Delete this thread?')) {
      deleteChatThread(threadId)
      setThreadsList(getThreadsList())
      if (threadId === currentThreadId) createNewThread()
    }
  }

  const handleSendMessage = () => {
    if (!inputValue.trim() || status !== 'connected') return
    const userMessage = inputValue.trim()
    setInputValue('')
    addMessage('user', userMessage)
    setIsGenerating(true)
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({
        type: 'generate',
        prompt: userMessage,
        projectName: projectName || 'my-website'
      }))
    }
  }

  const handlePaymentGatewaySelect = (gateway) => {
    setShowPaymentSelector(false)
    addMessage('user', `Selected: ${gateway}`)
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({ type: 'answer', answer: gateway }))
    }
  }

  const handleConsoleError = (error) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      addMessage('system', `🐛 Diagnosing: ${error.message}`)
      wsRef.current.send(JSON.stringify({
        type: 'console_error',
        error: error.message,
        filePath: selectedFile || 'unknown',
        allFiles: projectFiles,
        sessionId: projectSessionId
      }))
    }
  }

  const handleExportZIP = async () => {
    if (!Object.keys(projectFiles).length) return
    try {
      addMessage('system', '📦 Compressing files...')
      const zip = new JSZip()
      Object.entries(projectFiles).forEach(([path, content]) => zip.file(path, content))
      const blob = await zip.generateAsync({ type: 'blob' })
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `${projectName || 'project'}.zip`
      document.body.appendChild(a)
      a.click()
      document.body.removeChild(a)
      URL.revokeObjectURL(url)
    } catch (error) {
      addMessage('system', '❌ Export failed')
    }
  }

  return (
    <div className="app-container">
      {/* Ambient Background Elements */}
      <div className="ambient-orb primary"></div>
      <div className="ambient-orb secondary"></div>

      {/* Header */}
      <header className="glass-header">
        <div className="header-left">
          <button className="icon-btn" onClick={() => setShowThreadsList(!showThreadsList)}>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
          </button>
          <div className="brand">
            <span className="logo-icon">✨</span>
            <h1>Aether Builder</h1>
          </div>
        </div>
        <div style={{display: 'flex', gap: '10px', alignItems: 'center'}}>
          {Object.keys(projectFiles).length > 0 && (
            <button
              className="icon-btn"
              onClick={() => setShowPreview(!showPreview)}
              title={showPreview ? 'Hide Preview' : 'Show Preview'}
            >
              {showPreview ? '👁️' : '👁️‍🗨️'} Preview
            </button>
          )}
          <div className={`status-badge ${status}`}>
            <span className="status-dot"></span>
            {status === 'connected' ? 'System Online' : status === 'error' ? 'Connection Failed' : 'Reconnecting...'}
          </div>
        </div>
      </header>

      <div className="main-layout">
        {/* Sidebar */}
        <div className={`sidebar glass-panel ${showThreadsList ? 'visible' : ''}`}>
          <div className="sidebar-header">
            <h3>History</h3>
            <button className="new-chat-btn" onClick={createNewThread}>+ New</button>
          </div>
          <div className="thread-list">
            {threadsList.map(thread => (
              <div key={thread.id} className={`thread-item ${thread.id === currentThreadId ? 'active' : ''}`} onClick={() => loadThread(thread.id)}>
                <div className="thread-name">{thread.name}</div>
                <div className="thread-date">{new Date(thread.updatedAt).toLocaleDateString()}</div>
                <button className="delete-btn" onClick={(e) => { e.stopPropagation(); deleteThread(thread.id) }}>×</button>
              </div>
            ))}
          </div>
        </div>

        {/* Chat Area */}
        <div className="chat-section glass-panel">
          <div className="messages-container">
            {messages.map((msg, idx) => (
              <div key={idx} className={`message-row ${msg.type}`}>
                <div className="message-bubble">
                  {msg.type === 'assistant' && <div className="avatar">AI</div>}
                  <div className="content">
                    {msg.content}
                    {msg.data?.type === 'project' && (
                      <div className="project-card">
                        <div className="card-info">
                          <strong>{msg.data.projectName}</strong>
                          <span>{msg.data.projectType} • {msg.data.fileCount} files</span>
                        </div>
                        <button onClick={() => setShowPreview(true)}>Open Preview</button>
                      </div>
                    )}
                  </div>
                </div>
              </div>
            ))}
            {isGenerating && (
              <div className="message-row assistant">
                <div className="message-bubble loading">
                  <div className="typing-dots"><span></span><span></span><span></span></div>
                </div>
              </div>
            )}
            <div ref={chatEndRef} />
          </div>

          <div className="input-area">
            <div className="input-wrapper glass-inset">
              <textarea
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && !e.shiftKey && (e.preventDefault(), handleSendMessage())}
                placeholder="Describe your dream website..."
                disabled={isGenerating}
              />
              <button className="send-btn" onClick={handleSendMessage} disabled={!inputValue.trim() || isGenerating}>
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
              </button>
            </div>
          </div>
        </div>

        {/* Preview Area */}
        {showPreview && (
          <div className="preview-section glass-panel">
            <div className="preview-toolbar-header">
              <div className="project-meta">
                <span className="project-name">{projectName || 'Untitled'}</span>
                {liveUrl && <a href={liveUrl} target="_blank" className="live-tag">LIVE</a>}
              </div>
              <div className="preview-actions">
                <button onClick={handleExportZIP} title="Export ZIP">📦</button>
                <button onClick={() => setShowPreview(false)} title="Close">✕</button>
              </div>
            </div>

            <div className="preview-body">
              {!liveUrl && (
                <div className="file-sidebar">
                  <FileTree files={projectFiles} selectedFile={selectedFile} onSelectFile={setSelectedFile} />
                </div>
              )}
              
              <div className="preview-frame-container">
                {liveUrl ? (
                   <iframe src={liveUrl} className="live-frame" title="Live Preview" />
                ) : (
                   selectedFile && selectedFile.match(/\.(html|jsx?|tsx?|css)$/i) ? (
                    <PreviewV2 files={projectFiles} selectedFile={selectedFile} onConsoleError={handleConsoleError} />
                  ) : (
                    <div className="code-editor-view">
                      <pre>{projectFiles[selectedFile]}</pre>
                    </div>
                  )
                )}
              </div>
            </div>
          </div>
        )}
      </div>

      {showPaymentSelector && (
        <div className="modal-backdrop">
          <PaymentGatewaySelector question={paymentQuestion} options={paymentOptions} onSelect={handlePaymentGatewaySelect} />
        </div>
      )}
    </div>
  )
}

export default ChatApp