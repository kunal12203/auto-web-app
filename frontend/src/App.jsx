import { useState, useEffect, useRef } from 'react'
import './App.css'
import PromptInput from './components/PromptInput'
import Preview from './components/Preview'
import StatusBar from './components/StatusBar'

function App() {
  const [prompt, setPrompt] = useState('')
  const [generatedHTML, setGeneratedHTML] = useState('')
  const [status, setStatus] = useState('disconnected')
  const [statusMessage, setStatusMessage] = useState('Connecting to server...')
  const [conversationHistory, setConversationHistory] = useState([])
  const [sessionId, setSessionId] = useState(null)
  const wsRef = useRef(null)

  useEffect(() => {
    // Generate session ID on mount
    if (!sessionId) {
      setSessionId(Date.now().toString(36) + Math.random().toString(36).substr(2))
    }

    // Connect to WebSocket
    const connectWebSocket = () => {
      const ws = new WebSocket('ws://localhost:8000/ws')

      ws.onopen = () => {
        console.log('WebSocket connected')
        setStatus('connected')
        setStatusMessage('Ready to build!')
      }

      ws.onmessage = (event) => {
        const data = JSON.parse(event.data)

        if (data.type === 'status') {
          setStatus('generating')
          setStatusMessage(data.message)
        } else if (data.type === 'code') {
          setGeneratedHTML(data.html)
          // Add to conversation history
          setConversationHistory(prev => [...prev, {
            prompt: data.prompt,
            html: data.html,
            timestamp: new Date().toISOString()
          }])
          setStatus('success')
          setStatusMessage('Website generated successfully!')
          setTimeout(() => {
            setStatus('connected')
            setStatusMessage('Ready to build!')
          }, 2000)
        } else if (data.type === 'error') {
          setStatus('error')
          setStatusMessage(data.message)
          setTimeout(() => {
            setStatus('connected')
            setStatusMessage('Ready to build!')
          }, 3000)
        }
      }

      ws.onerror = (error) => {
        console.error('WebSocket error:', error)
        setStatus('error')
        setStatusMessage('Connection error. Please check if backend is running.')
      }

      ws.onclose = () => {
        console.log('WebSocket disconnected')
        setStatus('disconnected')
        setStatusMessage('Disconnected. Retrying...')
        // Retry connection after 3 seconds
        setTimeout(connectWebSocket, 3000)
      }

      wsRef.current = ws
    }

    connectWebSocket()

    // Cleanup on unmount
    return () => {
      if (wsRef.current) {
        wsRef.current.close()
      }
    }
  }, [])

  const handleGenerate = (promptText, isModification = false) => {
    if (!promptText.trim()) {
      setStatusMessage('Please enter a prompt')
      return
    }

    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({
        type: 'generate',
        prompt: promptText,
        conversationHistory: isModification ? conversationHistory : [],
        sessionId: sessionId,
        isModification: isModification
      }))
      setPrompt(promptText)
    } else {
      setStatus('error')
      setStatusMessage('Not connected to server')
    }
  }

  const handleExportCode = () => {
    if (!generatedHTML) {
      alert('No website generated yet!')
      return
    }

    const blob = new Blob([generatedHTML], { type: 'text/html' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `website-${sessionId}.html`
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)

    setStatusMessage('Code exported successfully!')
    setTimeout(() => {
      setStatus('connected')
      setStatusMessage('Ready to build!')
    }, 2000)
  }

  const handleNewWebsite = () => {
    setGeneratedHTML('')
    setConversationHistory([])
    setSessionId(Date.now().toString(36) + Math.random().toString(36).substr(2))
    setPrompt('')
    setStatusMessage('Ready to build a new website!')
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>🚀 AI Website Builder</h1>
        <p>Build websites with natural language prompts</p>
      </header>

      <StatusBar status={status} message={statusMessage} />

      <div className="app-content">
        <div className="left-panel">
          <PromptInput
            onGenerate={handleGenerate}
            disabled={status !== 'connected'}
            hasExistingWebsite={!!generatedHTML}
          />

          {generatedHTML && (
            <div className="action-buttons">
              <button
                className="action-btn export-btn"
                onClick={handleExportCode}
                title="Download HTML file"
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                  <polyline points="7 10 12 15 17 10"></polyline>
                  <line x1="12" y1="15" x2="12" y2="3"></line>
                </svg>
                Export Code
              </button>
              <button
                className="action-btn new-btn"
                onClick={handleNewWebsite}
                title="Start a new website"
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <line x1="12" y1="5" x2="12" y2="19"></line>
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                </svg>
                New Website
              </button>
            </div>
          )}

          {prompt && (
            <div className="current-prompt">
              <h3>Current Session:</h3>
              <p>{prompt}</p>
              {conversationHistory.length > 1 && (
                <div className="iteration-count">
                  Iteration #{conversationHistory.length}
                </div>
              )}
            </div>
          )}
        </div>

        <div className="right-panel">
          <Preview html={generatedHTML} />
        </div>
      </div>
    </div>
  )
}

export default App
