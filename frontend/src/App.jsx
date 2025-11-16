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
  const wsRef = useRef(null)

  useEffect(() => {
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

  const handleGenerate = (promptText) => {
    if (!promptText.trim()) {
      setStatusMessage('Please enter a prompt')
      return
    }

    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({
        type: 'generate',
        prompt: promptText
      }))
      setPrompt(promptText)
    } else {
      setStatus('error')
      setStatusMessage('Not connected to server')
    }
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
          <PromptInput onGenerate={handleGenerate} disabled={status !== 'connected'} />

          {prompt && (
            <div className="current-prompt">
              <h3>Current Prompt:</h3>
              <p>{prompt}</p>
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
