import { useState, useEffect, useRef } from 'react'
import JSZip from 'jszip'
import './App.css'
import PromptInput from './components/PromptInput'
import Preview from './components/Preview' // Uses the unified Preview component
import FileTree from './components/FileTree'
import PaymentGatewaySelector from './components/PaymentGatewaySelector'
import StatusBar from './components/StatusBar'
import BuildingAnimation from './components/BuildingAnimation'

// Storage utilities
import { generateThreadId } from './chatStorage' // Assumes this file exists from previous step

function App() {
  // State
  const [projectFiles, setProjectFiles] = useState({})
  const [projectName, setProjectName] = useState('')
  const [messages, setMessages] = useState([{ type: 'assistant', content: 'Ready to code. What are we building today?' }])
  const [status, setStatus] = useState('connected')
  const [statusMessage, setStatusMessage] = useState('System Online')
  const [selectedFile, setSelectedFile] = useState(null)
  const [isBuilding, setIsBuilding] = useState(false)
  const [sessionId, setSessionId] = useState(null)
  const [showPayment, setShowPayment] = useState(false)
  
  const wsRef = useRef(null)
  const chatEndRef = useRef(null)

  // Connect WS
  useEffect(() => {
    setSessionId(generateThreadId())
    const ws = new WebSocket('ws://localhost:8000/ws')
    ws.onopen = () => setStatus('connected')
    ws.onmessage = (e) => handleMessage(JSON.parse(e.data))
    ws.onclose = () => setStatus('disconnected')
    wsRef.current = ws
    return () => ws.close()
  }, [])

  // Auto-scroll chat
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const handleMessage = (data) => {
    switch(data.type) {
      case 'status':
        setStatusMessage(data.message)
        if (data.message.includes('Analyzing')) setIsBuilding(true)
        break
      case 'project':
        setProjectFiles(data.files)
        setProjectName(data.projectName)
        setMessages(prev => [...prev, { type: 'assistant', content: `Project "${data.projectName}" generated successfully.` }])
        setIsBuilding(false)
        setStatusMessage('Ready')
        if (Object.keys(data.files)[0]) setSelectedFile(Object.keys(data.files)[0])
        break
      case 'question':
        setMessages(prev => [...prev, { type: 'assistant', content: data.question }])
        setShowPayment(true) // Specific logic for payment question
        break
      case 'error':
        setIsBuilding(false)
        setMessages(prev => [...prev, { type: 'system', content: `Error: ${data.message}` }])
        break
      default: break
    }
  }

  const handleSend = (text) => {
    if (!text.trim()) return
    setMessages(prev => [...prev, { type: 'user', content: text }])
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({
        type: 'generate',
        prompt: text,
        sessionId
      }))
    }
  }

  const handlePaymentSelect = (choice) => {
    setShowPayment(false)
    setMessages(prev => [...prev, { type: 'user', content: `Selected: ${choice}` }])
    wsRef.current?.send(JSON.stringify({ type: 'answer', answer: choice }))
  }

  const handleConsoleError = (err) => {
    // Auto-fix logic
    wsRef.current?.send(JSON.stringify({
      type: 'console_error',
      error: err.message,
      allFiles: projectFiles
    }))
  }

  return (
    <div className="app">
      {isBuilding && <BuildingAnimation message={statusMessage} stage={1} totalStages={4} />}
      
      <header className="app-header">
        <div className="logo-group">
          <span style={{fontSize: '1.5rem'}}>🚀</span>
          <h1>Aether Builder</h1>
        </div>
        <StatusBar status={status} message={statusMessage} />
      </header>

      <div className="app-content">
        {/* Chat Panel */}
        <div className="chat-panel">
          <div className="chat-messages">
            {messages.map((m, i) => (
              <div key={i} className={`message ${m.type}`}>{m.content}</div>
            ))}
            <div ref={chatEndRef} />
          </div>
          <div className="chat-input-area">
            <PromptInput onGenerate={handleSend} disabled={isBuilding} />
          </div>
        </div>

        {/* Preview / File Panel */}
        <div className="preview-panel">
          {Object.keys(projectFiles).length > 0 ? (
            <>
              <div className="preview-panel-header">
                <span style={{fontSize:'0.9rem', color:'#888'}}>{projectName}</span>
                <div style={{display:'flex', gap:'10px'}}>
                   {/* Simple Export Button */}
                   <button 
                     onClick={() => alert('Exporting...')} 
                     style={{background:'none', border:'1px solid #333', color:'white', padding:'4px 8px', borderRadius:'4px', cursor:'pointer'}}
                   >
                     Export
                   </button>
                </div>
              </div>
              <div style={{flex: 1, display:'flex', overflow:'hidden'}}>
                <div style={{width:'200px', background:'#111', borderRight:'1px solid #222', overflowY:'auto'}}>
                   <FileTree files={projectFiles} selectedFile={selectedFile} onSelectFile={setSelectedFile} />
                </div>
                <div style={{flex: 1, position:'relative'}}>
                   <Preview files={projectFiles} selectedFile={selectedFile} onConsoleError={handleConsoleError} />
                </div>
              </div>
            </>
          ) : (
            <div style={{flex:1, display:'flex', alignItems:'center', justifyContent:'center', color:'#333'}}>
              <h2>Waiting for project generation...</h2>
            </div>
          )}
        </div>
      </div>

      {showPayment && (
        <div style={{position:'fixed', inset:0, background:'rgba(0,0,0,0.8)', zIndex:999, display:'flex', alignItems:'center', justifyContent:'center'}}>
          <PaymentGatewaySelector 
            question="Select Payment Gateway" 
            options={['Stripe', 'PayPal', 'Razorpay']} 
            onSelect={handlePaymentSelect} 
          />
        </div>
      )}
    </div>
  )
}

export default App