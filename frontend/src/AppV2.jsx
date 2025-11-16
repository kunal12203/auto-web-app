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
  // Project state
  const [projectFiles, setProjectFiles] = useState({})
  const [projectName, setProjectName] = useState('')
  const [projectType, setProjectType] = useState('')
  const [paymentGateway, setPaymentGateway] = useState(null)

  // UI state
  const [selectedFile, setSelectedFile] = useState(null)
  const [status, setStatus] = useState('disconnected')
  const [statusMessage, setStatusMessage] = useState('Connecting to server...')
  const [prompt, setPrompt] = useState('')

  // Building animation
  const [isBuilding, setIsBuilding] = useState(false)
  const [buildingStage, setBuildingStage] = useState(0)
  const [buildingMessage, setBuildingMessage] = useState('')

  // Payment gateway question
  const [showPaymentSelector, setShowPaymentSelector] = useState(false)
  const [paymentQuestion, setPaymentQuestion] = useState('')
  const [paymentOptions, setPaymentOptions] = useState([])
  const pendingQuestionResolve = useRef(null)

  // WebSocket
  const [sessionId, setSessionId] = useState(null)
  const wsRef = useRef(null)

  useEffect(() => {
    // Generate session ID
    if (!sessionId) {
      setSessionId(Date.now().toString(36) + Math.random().toString(36).substr(2))
    }

    // Connect to WebSocket
    const connectWebSocket = () => {
      const ws = new WebSocket('ws://localhost:8000/ws')

      ws.onopen = () => {
        console.log('WebSocket connected')
        setStatus('connected')
        setStatusMessage('Ready to build amazing projects!')
      }

      ws.onmessage = (event) => {
        const data = JSON.parse(event.data)
        handleWebSocketMessage(data)
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

  const handleWebSocketMessage = (data) => {
    switch (data.type) {
      case 'status':
        setStatus('generating')
        setStatusMessage(data.message)
        setBuildingMessage(data.message)

        // Update building stage based on message
        if (data.message.includes('Analyzing')) setBuildingStage(0)
        else if (data.message.includes('Generating')) setBuildingStage(2)
        else if (data.message.includes('Writing')) setBuildingStage(3)
        else if (data.message.includes('Setting')) setBuildingStage(5)

        break

      case 'question':
        // Backend is asking a question (payment gateway)
        setPaymentQuestion(data.question)
        setPaymentOptions(data.options)
        setShowPaymentSelector(true)
        break

      case 'project':
        // Received complete project
        setIsBuilding(false)
        setProjectFiles(data.files)
        setProjectName(data.projectName)
        setProjectType(data.projectType)
        setPaymentGateway(data.paymentGateway)

        // Auto-select first file to display
        const firstFile = Object.keys(data.files)[0]
        if (firstFile) {
          setSelectedFile(firstFile)
        }

        setStatus('success')
        setStatusMessage(`🎉 ${data.projectType.toUpperCase()} project generated! ${Object.keys(data.files).length} files created.`)

        setTimeout(() => {
          setStatus('connected')
          setStatusMessage('Ready to build!')
        }, 3000)
        break

      case 'file_updated':
        // A specific file was updated
        setProjectFiles(prev => ({
          ...prev,
          [data.filePath]: data.content
        }))

        if (data.fixed) {
          setStatusMessage(`✅ Fixed error in ${data.filePath}`)
        } else {
          setStatusMessage(`Updated ${data.filePath}`)
        }

        setTimeout(() => {
          setStatus('connected')
          setStatusMessage('Ready to build!')
        }, 2000)
        break

      case 'error':
        setIsBuilding(false)
        setStatus('error')
        setStatusMessage(data.message)
        setTimeout(() => {
          setStatus('connected')
          setStatusMessage('Ready to build!')
        }, 3000)
        break
    }
  }

  const handleGenerate = (promptText, isModification = false) => {
    if (!promptText.trim()) {
      setStatusMessage('Please enter a prompt')
      return
    }

    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      setIsBuilding(true)
      setBuildingStage(0)
      setBuildingMessage('Starting to build your project...')

      wsRef.current.send(JSON.stringify({
        type: 'generate',
        prompt: promptText,
        projectName: projectName || 'my-website',
        sessionId: sessionId
      }))

      setPrompt(promptText)
    } else {
      setStatus('error')
      setStatusMessage('Not connected to server')
    }
  }

  const handlePaymentGatewaySelect = (gateway) => {
    setShowPaymentSelector(false)

    // Send answer back to backend
    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({
        type: 'answer',
        answer: gateway
      }))
    }
  }

  const handleConsoleError = (error) => {
    // Send console error to backend for fixing
    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({
        type: 'console_error',
        error: error.message,
        filePath: selectedFile || 'unknown',
        allFiles: projectFiles
      }))

      setStatusMessage('🔧 AI is fixing the error...')
    }
  }

  const handleExportZIP = async () => {
    if (!projectFiles || Object.keys(projectFiles).length === 0) {
      alert('No project to export!')
      return
    }

    try {
      setStatusMessage('Creating ZIP file...')

      const zip = new JSZip()

      // Add all files to ZIP maintaining folder structure
      Object.entries(projectFiles).forEach(([path, content]) => {
        zip.file(path, content)
      })

      // Generate ZIP
      const blob = await zip.generateAsync({ type: 'blob' })

      // Download
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `${projectName || 'project'}.zip`
      document.body.appendChild(a)
      a.click()
      document.body.removeChild(a)
      URL.revokeObjectURL(url)

      setStatusMessage('✅ Project exported successfully!')
      setTimeout(() => {
        setStatus('connected')
        setStatusMessage('Ready to build!')
      }, 2000)
    } catch (error) {
      console.error('Export error:', error)
      setStatusMessage('❌ Export failed')
    }
  }

  const handleNewProject = () => {
    setProjectFiles({})
    setProjectName('')
    setProjectType('')
    setPaymentGateway(null)
    setSelectedFile(null)
    setPrompt('')
    setSessionId(Date.now().toString(36) + Math.random().toString(36).substr(2))
    setStatusMessage('Ready to build a new project!')
  }

  const hasProject = Object.keys(projectFiles).length > 0

  return (
    <div className="app">
      {/* Building Animation Overlay */}
      {isBuilding && (
        <BuildingAnimation
          message={buildingMessage}
          stage={buildingStage}
          totalStages={8}
        />
      )}

      {/* Payment Gateway Selector Modal */}
      {showPaymentSelector && (
        <PaymentGatewaySelector
          question={paymentQuestion}
          options={paymentOptions}
          onSelect={handlePaymentGatewaySelect}
        />
      )}

      {/* Header */}
      <header className="app-header">
        <div className="header-content">
          <div className="logo-section">
            <div className="logo-icon">🚀</div>
            <div>
              <h1>AI Website Builder</h1>
              <p>Production-ready projects in seconds</p>
            </div>
          </div>

          {hasProject && (
            <div className="project-info">
              <span className="project-badge">{projectType}</span>
              {paymentGateway && (
                <span className="payment-badge">💳 {paymentGateway}</span>
              )}
              <span className="files-count">{Object.keys(projectFiles).length} files</span>
            </div>
          )}
        </div>
      </header>

      <StatusBar status={status} message={statusMessage} />

      <div className="app-content">
        <div className="left-panel">
          <PromptInput
            onGenerate={handleGenerate}
            disabled={status !== 'connected'}
            hasExistingWebsite={hasProject}
          />

          {hasProject && (
            <>
              <div className="action-buttons">
                <button
                  className="action-btn export-zip-btn"
                  onClick={handleExportZIP}
                  title="Download complete project as ZIP"
                >
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                    <polyline points="7 10 12 15 17 10"></polyline>
                    <line x1="12" y1="15" x2="12" y2="3"></line>
                  </svg>
                  Export ZIP
                </button>
                <button
                  className="action-btn new-btn"
                  onClick={handleNewProject}
                  title="Start a new project"
                >
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <line x1="12" y1="5" x2="12" y2="19"></line>
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                  </svg>
                  New Project
                </button>
              </div>

              <div className="file-explorer">
                <FileTree
                  files={projectFiles}
                  selectedFile={selectedFile}
                  onSelectFile={setSelectedFile}
                />
              </div>

              {selectedFile && (
                <div className="file-viewer">
                  <div className="file-viewer-header">
                    <span className="file-icon">📄</span>
                    <span className="file-path">{selectedFile}</span>
                  </div>
                  <div className="file-content">
                    <pre><code>{projectFiles[selectedFile]}</code></pre>
                  </div>
                </div>
              )}

              {prompt && (
                <div className="current-prompt">
                  <h3>Current Project:</h3>
                  <p>{prompt}</p>
                </div>
              )}
            </>
          )}
        </div>

        <div className="right-panel">
          <PreviewV2
            files={projectFiles}
            projectType={projectType}
            onConsoleError={handleConsoleError}
          />
        </div>
      </div>
    </div>
  )
}

export default AppV2
