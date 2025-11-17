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

  // Chat state
  const [messages, setMessages] = useState([
    {
      type: 'assistant',
      content: '👋 Hey! I\'m your AI Website Builder. Tell me what you want to build and I\'ll create a production-ready project for you!',
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

  // Initialize thread on mount
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
        // Create new thread if saved one doesn't exist
        const newThreadId = generateThreadId()
        setCurrentThreadIdState(newThreadId)
        setCurrentThread(newThreadId)
      }
    } else {
      // Create new thread
      const newThreadId = generateThreadId()
      setCurrentThreadIdState(newThreadId)
      setCurrentThread(newThreadId)
    }

    // Load threads list
    setThreadsList(getThreadsList())
  }, [])

  // Auto-save thread whenever messages or project data changes
  useEffect(() => {
    if (currentThreadId && messages.length > 0) {
      autoSaveThread(currentThreadId, messages, {
        projectFiles,
        projectName,
        projectType,
        paymentGateway,
        projectSessionId
      })

      // Update threads list
      setThreadsList(getThreadsList())
    }
  }, [messages, projectFiles, projectName, projectType, paymentGateway, projectSessionId, currentThreadId])

  // Auto-scroll to bottom of chat
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  // WebSocket connection
  useEffect(() => {
    const connectWebSocket = () => {
      const ws = new WebSocket('ws://localhost:8000/ws')

      ws.onopen = () => {
        console.log('WebSocket connected')
        setStatus('connected')
        addMessage('system', '✅ Connected to server')
      }

      ws.onmessage = (event) => {
        const data = JSON.parse(event.data)
        handleWebSocketMessage(data)
      }

      ws.onerror = (error) => {
        console.error('WebSocket error:', error)
        setStatus('error')
        addMessage('system', '❌ Connection error. Please check if backend is running.')
      }

      ws.onclose = () => {
        console.log('WebSocket disconnected')
        setStatus('disconnected')
        addMessage('system', '🔄 Disconnected. Retrying...')
        setTimeout(connectWebSocket, 3000)
      }

      wsRef.current = ws
    }

    connectWebSocket()

    return () => {
      if (wsRef.current) {
        wsRef.current.close()
      }
    }
  }, [])

  const addMessage = (type, content, data = null) => {
    setMessages(prev => [...prev, {
      type, // 'user', 'assistant', 'system'
      content,
      data,
      timestamp: new Date()
    }])
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

        console.log('✅ Project memory session:', data.sessionId)

        // Auto-select first file
        const firstFile = Object.keys(data.files)[0]
        if (firstFile) {
          setSelectedFile(firstFile)
        }

        setShowPreview(true)

        addMessage('assistant', `🎉 Your ${data.projectType.toUpperCase()} project is ready!`, {
          type: 'project',
          fileCount: Object.keys(data.files).length,
          projectType: data.projectType,
          projectName: data.projectName
        })
        break

      case 'file_updated':
        setProjectFiles(prev => ({
          ...prev,
          [data.filePath]: data.content
        }))

        if (data.fixed) {
          addMessage('assistant', `✅ Fixed error in ${data.filePath}`)
        } else {
          addMessage('assistant', `✅ Updated ${data.filePath}`)
        }
        break

      case 'error':
        setIsGenerating(false)
        addMessage('system', `❌ Error: ${data.message}`)
        break

      default:
        break
    }
  }

  // Thread management functions
  const createNewThread = () => {
    const newThreadId = generateThreadId()
    setCurrentThreadIdState(newThreadId)
    setCurrentThread(newThreadId)

    // Reset state for new chat
    setMessages([
      {
        type: 'assistant',
        content: '👋 Hey! I\'m your AI Website Builder. Tell me what you want to build and I\'ll create a production-ready project for you!',
        timestamp: new Date()
      }
    ])
    setProjectFiles({})
    setProjectName('')
    setProjectType('')
    setPaymentGateway(null)
    setProjectSessionId(null)
    setShowPreview(false)
    setSelectedFile(null)
    setShowThreadsList(false)

    addMessage('system', '✨ Started new chat thread')
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
    if (confirm('Are you sure you want to delete this chat thread?')) {
      deleteChatThread(threadId)
      setThreadsList(getThreadsList())

      // If deleting current thread, create a new one
      if (threadId === currentThreadId) {
        createNewThread()
      }
    }
  }

  const handleSendMessage = () => {
    if (!inputValue.trim() || status !== 'connected') return

    const userMessage = inputValue.trim()
    setInputValue('')

    // Add user message to chat
    addMessage('user', userMessage)

    // Show loading
    setIsGenerating(true)
    addMessage('assistant', '🤔 Analyzing your requirements...')

    // Send to backend
    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
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

    // Send answer back to backend
    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({
        type: 'answer',
        answer: gateway
      }))
    }
  }

  const handleConsoleError = (error) => {
    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      addMessage('system', `🐛 Detected error: ${error.message}`)
      addMessage('assistant', '🔧 Fixing the error...')

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
    if (!projectFiles || Object.keys(projectFiles).length === 0) {
      addMessage('system', '⚠️ No project to export!')
      return
    }

    try {
      addMessage('system', '📦 Creating ZIP file...')
      const zip = new JSZip()

      Object.entries(projectFiles).forEach(([path, content]) => {
        zip.file(path, content)
      })

      const blob = await zip.generateAsync({ type: 'blob' })
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `${projectName || 'project'}.zip`
      document.body.appendChild(a)
      a.click()
      document.body.removeChild(a)
      URL.revokeObjectURL(url)

      addMessage('assistant', '✅ Project exported successfully!')
    } catch (error) {
      console.error('Export error:', error)
      addMessage('system', '❌ Export failed')
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSendMessage()
    }
  }

  return (
    <div className="chat-app">
      {/* Threads Sidebar */}
      {showThreadsList && (
        <div className="threads-sidebar">
          <div className="threads-header">
            <h3>Chat Threads</h3>
            <button className="close-threads" onClick={() => setShowThreadsList(false)}>✕</button>
          </div>
          <button className="new-thread-btn" onClick={createNewThread}>
            ➕ New Chat
          </button>
          <div className="threads-list">
            {threadsList.length === 0 ? (
              <div className="no-threads">No saved threads yet</div>
            ) : (
              threadsList.map(thread => (
                <div
                  key={thread.id}
                  className={`thread-item ${thread.id === currentThreadId ? 'active' : ''}`}
                >
                  <div className="thread-info" onClick={() => loadThread(thread.id)}>
                    <div className="thread-name">{thread.name}</div>
                    <div className="thread-meta">
                      {thread.messageCount} messages • {new Date(thread.updatedAt).toLocaleDateString()}
                    </div>
                  </div>
                  <button
                    className="delete-thread-btn"
                    onClick={(e) => {
                      e.stopPropagation()
                      deleteThread(thread.id)
                    }}
                  >
                    🗑️
                  </button>
                </div>
              ))
            )}
          </div>
        </div>
      )}

      {/* Left side - Chat */}
      <div className="chat-container">
        <div className="chat-header">
          <div className="chat-header-left">
            <button className="threads-toggle-btn" onClick={() => setShowThreadsList(!showThreadsList)}>
              ☰
            </button>
            <h1>🚀 AI Website Builder</h1>
          </div>
          <div className={`status-indicator ${status}`}>
            {status === 'connected' && '🟢 Connected'}
            {status === 'disconnected' && '🔴 Disconnected'}
            {status === 'error' && '⚠️ Error'}
          </div>
        </div>

        <div className="chat-messages">
          {messages.map((msg, idx) => (
            <div key={idx} className={`message ${msg.type}`}>
              {msg.type === 'user' && (
                <div className="message-bubble user-bubble">
                  <div className="message-content">{msg.content}</div>
                </div>
              )}

              {msg.type === 'assistant' && (
                <div className="message-bubble assistant-bubble">
                  <div className="message-avatar">🤖</div>
                  <div className="message-content">
                    {msg.content}
                    {msg.data?.type === 'project' && (
                      <div className="project-card">
                        <div className="project-info">
                          <strong>📂 {msg.data.projectName}</strong>
                          <span>{msg.data.fileCount} files • {msg.data.projectType}</span>
                        </div>
                        <button onClick={() => setShowPreview(true)}>
                          View Project →
                        </button>
                      </div>
                    )}
                  </div>
                </div>
              )}

              {msg.type === 'system' && (
                <div className="message-bubble system-bubble">
                  <div className="message-content">{msg.content}</div>
                </div>
              )}
            </div>
          ))}

          {isGenerating && (
            <div className="message assistant">
              <div className="message-bubble assistant-bubble typing">
                <div className="message-avatar">🤖</div>
                <div className="typing-indicator">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </div>
          )}

          <div ref={chatEndRef} />
        </div>

        <div className="chat-input-container">
          <textarea
            className="chat-input"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Describe the website you want to build... (Press Enter to send)"
            disabled={status !== 'connected' || isGenerating}
            rows="3"
          />
          <button
            className="send-button"
            onClick={handleSendMessage}
            disabled={!inputValue.trim() || status !== 'connected' || isGenerating}
          >
            {isGenerating ? '⏳' : '🚀'} Send
          </button>
        </div>

        <div className="chat-footer">
          {projectFiles && Object.keys(projectFiles).length > 0 && (
            <button className="export-button" onClick={handleExportZIP}>
              📦 Export as ZIP
            </button>
          )}
        </div>
      </div>

      {/* Right side - Preview (shows when project is generated) */}
      {showPreview && projectFiles && Object.keys(projectFiles).length > 0 && (
        <div className="preview-container">
          <div className="preview-header">
            <h2>📂 {projectName}</h2>
            <button className="close-preview" onClick={() => setShowPreview(false)}>
              ✕
            </button>
          </div>

          <div className="preview-content">
            <div className="file-tree-panel">
              <FileTree
                files={projectFiles}
                selectedFile={selectedFile}
                onSelectFile={setSelectedFile}
              />
            </div>

            <div className="preview-panel">
              {selectedFile && (
                <>
                  <div className="file-header">
                    <span className="file-name">{selectedFile}</span>
                  </div>

                  {selectedFile.match(/\.(html|jsx?|tsx?|css)$/i) ? (
                    <PreviewV2
                      files={projectFiles}
                      selectedFile={selectedFile}
                      onConsoleError={handleConsoleError}
                    />
                  ) : (
                    <pre className="code-view">
                      {projectFiles[selectedFile]}
                    </pre>
                  )}
                </>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Payment Gateway Selector Modal */}
      {showPaymentSelector && (
        <div className="modal-overlay">
          <PaymentGatewaySelector
            question={paymentQuestion}
            options={paymentOptions}
            onSelect={handlePaymentGatewaySelect}
          />
        </div>
      )}
    </div>
  )
}

export default ChatApp
