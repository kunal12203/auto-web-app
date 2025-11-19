import { useState, useEffect, useRef } from 'react'
import './App_old.css'
import Preview from './components/Preview'
import StatusBar from './components/StatusBar'

function AppOld() {
  const [prompt, setPrompt] = useState('')
  const [files, setFiles] = useState({}) // Stores generated files
  const [status, setStatus] = useState('connected')
  const [statusMessage, setStatusMessage] = useState('Legacy Mode: Ready')
  const [history, setHistory] = useState([])
  
  // Mock generation for legacy demo (or connect to real WS if needed)
  const handleGenerate = () => {
    if (!prompt.trim()) return
    
    setStatus('generating')
    setStatusMessage('Generating legacy project...')
    
    // Simulate API call
    setTimeout(() => {
      const newFiles = {
        'index.html': `<!DOCTYPE html>
<html>
<head>
  <style>body { font-family: sans-serif; background: #f0f0f0; color: #333; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; } .card { background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }</style>
</head>
<body>
  <div class="card">
    <h1>Legacy Generator</h1>
    <p>Generated from prompt: ${prompt}</p>
    <button onclick="alert('Hello!')">Click Me</button>
  </div>
</body>
</html>`
      }
      
      setFiles(newFiles)
      setHistory(prev => [{ prompt, timestamp: new Date() }, ...prev])
      setStatus('success')
      setStatusMessage('Generation Complete')
      setTimeout(() => setStatus('connected'), 2000)
    }, 2000)
  }

  return (
    <div className="app-old">
      <header className="old-header">
        <h1>Aether Builder (Legacy)</h1>
        <p>Standard Prompt-to-Code Interface</p>
      </header>

      <StatusBar status={status} message={statusMessage} />

      <div className="old-content">
        <div className="old-sidebar">
          <div className="prompt-card">
            <h3>Input Prompt</h3>
            <textarea 
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Describe a website..."
            />
            <button className="generate-btn" onClick={handleGenerate}>
              Generate Website
            </button>
          </div>

          <div className="history-section">
            <h3>History</h3>
            <div className="history-list">
              {history.map((item, i) => (
                <div key={i} className="history-item">
                  {item.prompt}
                  <br/>
                  <small style={{opacity:0.5}}>{item.timestamp.toLocaleTimeString()}</small>
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="old-preview-area">
          <Preview files={files} />
        </div>
      </div>
    </div>
  )
}

export default AppOld