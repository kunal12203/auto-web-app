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
  const [currentHistoryIndex, setCurrentHistoryIndex] = useState(-1)
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
          setConversationHistory(prev => {
            const newHistory = [...prev, {
              prompt: data.prompt,
              html: data.html,
              timestamp: new Date().toISOString()
            }]
            setCurrentHistoryIndex(newHistory.length - 1)
            return newHistory
          })
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
    setCurrentHistoryIndex(-1)
    setSessionId(Date.now().toString(36) + Math.random().toString(36).substr(2))
    setPrompt('')
    setStatusMessage('Ready to build a new website!')
  }

  const handleUndo = () => {
    if (currentHistoryIndex > 0) {
      const newIndex = currentHistoryIndex - 1
      setCurrentHistoryIndex(newIndex)
      setGeneratedHTML(conversationHistory[newIndex].html)
      setPrompt(conversationHistory[newIndex].prompt)
      setStatusMessage(`Reverted to version ${newIndex + 1}`)
      setTimeout(() => {
        setStatus('connected')
        setStatusMessage('Ready to build!')
      }, 2000)
    }
  }

  const handleRedo = () => {
    if (currentHistoryIndex < conversationHistory.length - 1) {
      const newIndex = currentHistoryIndex + 1
      setCurrentHistoryIndex(newIndex)
      setGeneratedHTML(conversationHistory[newIndex].html)
      setPrompt(conversationHistory[newIndex].prompt)
      setStatusMessage(`Restored to version ${newIndex + 1}`)
      setTimeout(() => {
        setStatus('connected')
        setStatusMessage('Ready to build!')
      }, 2000)
    }
  }

  const handleExportProject = () => {
    if (!generatedHTML) {
      alert('No website generated yet!')
      return
    }

    // Parse HTML to extract CSS and JS
    const parser = new DOMParser()
    const doc = parser.parseFromString(generatedHTML, 'text/html')

    // Extract styles
    const styleElements = doc.querySelectorAll('style')
    let cssContent = '/* Generated CSS */\n\n'
    styleElements.forEach((style, index) => {
      cssContent += `/* Style Block ${index + 1} */\n${style.textContent}\n\n`
    })

    // Extract scripts
    const scriptElements = doc.querySelectorAll('script')
    let jsContent = '/* Generated JavaScript */\n\n'
    scriptElements.forEach((script, index) => {
      if (script.textContent) {
        jsContent += `/* Script Block ${index + 1} */\n${script.textContent}\n\n`
      }
    })

    // Create modified HTML with external links
    let modifiedHTML = generatedHTML
    modifiedHTML = modifiedHTML.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '<link rel="stylesheet" href="styles.css">')
    modifiedHTML = modifiedHTML.replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
    modifiedHTML = modifiedHTML.replace('</body>', '<script src="script.js"></script>\n</body>')

    // Create README content
    const readmeContent = `# ${prompt || 'AI Generated Website'}

Generated on: ${new Date().toLocaleString()}
Session ID: ${sessionId}

## Project Structure

- \`index.html\` - Main HTML file
- \`styles.css\` - Stylesheet
- \`script.js\` - JavaScript functionality
- \`README.md\` - This file

## How to Run

1. Open \`index.html\` in a web browser
2. Or use a local server:
   \`\`\`bash
   # Using Python
   python -m http.server 8000

   # Using Node.js
   npx http-server
   \`\`\`

## Deployment

This project can be deployed to:
- GitHub Pages
- Netlify
- Vercel
- Any static hosting service

Simply upload all files to your hosting provider.

## Modifications

To modify this website:
- Edit \`index.html\` for structure
- Edit \`styles.css\` for styling
- Edit \`script.js\` for interactivity

---

Generated by AI Website Builder
`

    // Create package.json for modern deployment
    const packageJson = {
      name: `website-${sessionId}`,
      version: '1.0.0',
      description: prompt || 'AI Generated Website',
      scripts: {
        start: 'npx http-server -p 8000',
        deploy: 'echo "Deploy to your preferred hosting service"'
      },
      keywords: ['website', 'ai-generated'],
      author: '',
      license: 'MIT'
    }

    // Create download function with multiple files
    const downloadProject = () => {
      // Create a simple way to download multiple files
      // Since we can't create ZIP in browser easily without library,
      // we'll download files individually with instructions

      const files = [
        { name: 'index.html', content: modifiedHTML, type: 'text/html' },
        { name: 'styles.css', content: cssContent, type: 'text/css' },
        { name: 'script.js', content: jsContent, type: 'text/javascript' },
        { name: 'README.md', content: readmeContent, type: 'text/markdown' },
        { name: 'package.json', content: JSON.stringify(packageJson, null, 2), type: 'application/json' }
      ]

      // Download all files
      files.forEach((file, index) => {
        setTimeout(() => {
          const blob = new Blob([file.content], { type: file.type })
          const url = URL.createObjectURL(blob)
          const a = document.createElement('a')
          a.href = url
          a.download = file.name
          document.body.appendChild(a)
          a.click()
          document.body.removeChild(a)
          URL.revokeObjectURL(url)
        }, index * 300) // Stagger downloads
      })

      setStatusMessage(`Exporting ${files.length} files...`)
      setTimeout(() => {
        setStatus('success')
        setStatusMessage('Project exported successfully!')
        setTimeout(() => {
          setStatus('connected')
          setStatusMessage('Ready to build!')
        }, 2000)
      }, files.length * 300 + 500)
    }

    downloadProject()
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
            <>
              <div className="history-controls">
                <button
                  className="history-btn"
                  onClick={handleUndo}
                  disabled={currentHistoryIndex <= 0}
                  title="Undo - Go to previous version"
                >
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M3 7v6h6"></path>
                    <path d="M21 17a9 9 0 0 0-9-9 9 9 0 0 0-6 2.3L3 13"></path>
                  </svg>
                  Undo
                </button>
                <div className="version-indicator">
                  Version {currentHistoryIndex + 1} / {conversationHistory.length}
                </div>
                <button
                  className="history-btn"
                  onClick={handleRedo}
                  disabled={currentHistoryIndex >= conversationHistory.length - 1}
                  title="Redo - Go to next version"
                >
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M21 7v6h-6"></path>
                    <path d="M3 17a9 9 0 0 1 9-9 9 9 0 0 1 6 2.3l3 2.7"></path>
                  </svg>
                  Redo
                </button>
              </div>

              <div className="action-buttons">
                <button
                  className="action-btn export-btn"
                  onClick={handleExportCode}
                  title="Download single HTML file"
                >
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                    <polyline points="7 10 12 15 17 10"></polyline>
                    <line x1="12" y1="15" x2="12" y2="3"></line>
                  </svg>
                  Export HTML
                </button>
                <button
                  className="action-btn project-btn"
                  onClick={handleExportProject}
                  title="Download complete project folder"
                >
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
                    <path d="M12 11v6m-3-3l3 3 3-3"></path>
                  </svg>
                  Export Project
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
            </>
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
