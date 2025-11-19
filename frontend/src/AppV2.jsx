import { useState, useEffect, useRef } from 'react'
import JSZip from 'jszip'
import './AppV2.css'
import PromptInput from './components/PromptInput'
import PreviewV2 from './components/PreviewV2'
import FileTree from './components/FileTree'
import PaymentGatewaySelector from './components/PaymentGatewaySelector'
import BuildingAnimation from './components/BuildingAnimation'
import StatusBar from './components/StatusBar'

function AppV2() {
  const [projectFiles, setProjectFiles] = useState({})
  const [projectName, setProjectName] = useState('')
  const [projectType, setProjectType] = useState('')
  const [paymentGateway, setPaymentGateway] = useState(null)
  const [projectSessionId, setProjectSessionId] = useState(null)
  const [selectedFile, setSelectedFile] = useState(null)
  const [status, setStatus] = useState('disconnected')
  const [statusMessage, setStatusMessage] = useState('Connecting to neural network...')
  const [prompt, setPrompt] = useState('')
  const [isBuilding, setIsBuilding] = useState(false)
  const [buildingStage, setBuildingStage] = useState(0)
  const [buildingMessage, setBuildingMessage] = useState('')
  const [showPaymentSelector, setShowPaymentSelector] = useState(false)
  const [paymentQuestion, setPaymentQuestion] = useState('')
  const [paymentOptions, setPaymentOptions] = useState([])
  const [sessionId, setSessionId] = useState(null)
  const wsRef = useRef(null)

  useEffect(() => {
    if (!sessionId) setSessionId(Date.now().toString(36) + Math.random().toString(36).substr(2))
    
    const connectWebSocket = () => {
      const ws = new WebSocket('ws://localhost:8000/ws')
      ws.onopen = () => {
        console.log('Connected')
        setStatus('connected')
        setStatusMessage('System Online. Ready to build.')
      }
      ws.onmessage = (event) => {
        const data = JSON.parse(event.data)
        handleWebSocketMessage(data)
      }
      ws.onerror = () => {
        setStatus('error')
        setStatusMessage('Connection lost. Retrying...')
      }
      ws.onclose = () => {
        setStatus('disconnected')
        setTimeout(connectWebSocket, 3000)
      }
      wsRef.current = ws
    }
    connectWebSocket()
    return () => wsRef.current?.close()
  }, [])

  const handleWebSocketMessage = (data) => {
    switch (data.type) {
      case 'status':
        setStatus('generating')
        setStatusMessage(data.message)
        setBuildingMessage(data.message)
        if (data.message.includes('Analyzing')) setBuildingStage(1)
        if (data.message.includes('Generating')) setBuildingStage(3)
        if (data.message.includes('Writing')) setBuildingStage(5)
        break
      case 'question':
        setPaymentQuestion(data.question)
        setPaymentOptions(data.options)
        setShowPaymentSelector(true)
        break
      case 'project':
        setIsBuilding(false)
        setProjectFiles(data.files)
        setProjectName(data.projectName)
        setProjectType(data.projectType)
        setPaymentGateway(data.paymentGateway)
        setProjectSessionId(data.sessionId)
        if (Object.keys(data.files)[0]) setSelectedFile(Object.keys(data.files)[0])
        setStatus('success')
        setStatusMessage('Project Generation Complete.')
        setTimeout(() => setStatus('connected'), 3000)
        break
      case 'file_updated':
        setProjectFiles(prev => ({ ...prev, [data.filePath]: data.content }))
        setStatusMessage(`Updated: ${data.filePath}`)
        break
      case 'error':
        setIsBuilding(false)
        setStatus('error')
        setStatusMessage(data.message)
        break
      default: break
    }
  }

  const handleGenerate = (promptText) => {
    if (!promptText.trim()) return
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      setIsBuilding(true)
      setBuildingStage(0)
      setBuildingMessage('Initializing creative sequence...')
      wsRef.current.send(JSON.stringify({
        type: 'generate',
        prompt: promptText,
        projectName: projectName || 'my-website',
        sessionId: sessionId
      }))
      setPrompt(promptText)
    }
  }

  const handlePaymentGatewaySelect = (gateway) => {
    setShowPaymentSelector(false)
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({ type: 'answer', answer: gateway }))
    }
  }

  const handleConsoleError = (error) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({
        type: 'console_error',
        error: error.message,
        filePath: selectedFile || 'unknown',
        allFiles: projectFiles,
        sessionId: projectSessionId
      }))
      setStatusMessage('Auto-fixing detected error...')
    }
  }

  const handleExportZIP = async () => {
    if (!Object.keys(projectFiles).length) return
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
  }

  return (
    <div className="app">
      {isBuilding && <BuildingAnimation message={buildingMessage} stage={buildingStage} totalStages={8} />}
      
      {showPaymentSelector && (
        <div className="modal-backdrop" style={{position:'fixed',top:0,left:0,right:0,bottom:0,zIndex:1000,background:'rgba(0,0,0,0.7)',display:'flex',alignItems:'center',justifyContent:'center'}}>
          <PaymentGatewaySelector question={paymentQuestion} options={paymentOptions} onSelect={handlePaymentGatewaySelect} />
        </div>
      )}

      <header className="app-header">
        <div className="header-content">
          <div className="logo-section">
            <div className="logo-icon">🚀</div>
            <div>
              <h1>Aether Builder</h1>
              <p>AI-Powered Development Environment</p>
            </div>
          </div>
          
          {Object.keys(projectFiles).length > 0 && (
            <div className="project-info">
              <div className="glass-badge">
                <span className="dot-indicator"></span>
                {projectType || 'Web Project'}
              </div>
              {paymentGateway && <div className="glass-badge">💳 {paymentGateway}</div>}
              <div className="glass-badge">📄 {Object.keys(projectFiles).length} Files</div>
            </div>
          )}
        </div>
      </header>

      <StatusBar status={status} message={statusMessage} />

      <div className="app-content">
        <div className="left-panel">
          <PromptInput onGenerate={handleGenerate} disabled={status !== 'connected'} hasExistingWebsite={Object.keys(projectFiles).length > 0} />
          
          {Object.keys(projectFiles).length > 0 && (
            <>
              <div className="action-buttons">
                <button className="action-btn" onClick={handleExportZIP}>
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  Export ZIP
                </button>
                <button className="action-btn primary-btn" onClick={() => setProjectFiles({})}>
                  <span>+</span> New Project
                </button>
              </div>
              
              <div className="file-explorer-panel">
                <FileTree files={projectFiles} selectedFile={selectedFile} onSelectFile={setSelectedFile} />
                {selectedFile && (
                  <div className="file-viewer">
                    <div className="file-viewer-header">
                      <span>📄 {selectedFile}</span>
                    </div>
                    <div className="file-content">
                      <pre><code>{projectFiles[selectedFile]}</code></pre>
                    </div>
                  </div>
                )}
              </div>
            </>
          )}
        </div>

        <div className="right-panel">
          <PreviewV2 files={projectFiles} selectedFile={selectedFile} onConsoleError={handleConsoleError} />
        </div>
      </div>
    </div>
  )
}

export default AppV2