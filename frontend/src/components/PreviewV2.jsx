import { useEffect, useRef, useState } from 'react'
import './Preview.css'

function PreviewV2({ files, selectedFile, onConsoleError }) {
  const iframeRef = useRef(null)
  const [deviceMode, setDeviceMode] = useState('desktop')

  // Helper to generate HTML blob
  const generateHTML = () => {
    // Simplified logic for brevity - assumes index.html exists
    // In a real app, you'd inject JS/CSS here like in previous versions
    if (!files['index.html']) return '<h1>No index.html found</h1>'
    
    let html = files['index.html']
    // Basic CSS injection for preview
    html = html.replace('<head>', `<head><style>
      /* Inject CSS files */
      ${Object.keys(files).filter(f => f.endsWith('.css')).map(f => files[f]).join('\n')}
    </style>`)
    return html
  }

  useEffect(() => {
    const html = generateHTML()
    if (iframeRef.current) {
      const doc = iframeRef.current.contentDocument
      doc.open()
      doc.write(html)
      doc.close()
      
      // Catch errors
      iframeRef.current.contentWindow.onerror = (msg) => {
        if (onConsoleError) onConsoleError({ message: msg })
      }
    }
  }, [files, selectedFile])

  return (
    <div className="preview-container-v2">
      <div className="device-toolbar">
        <div className="url-bar">
          <span className="lock-icon">🔒</span>
          <span>localhost:3000</span>
        </div>
        <div className="device-toggles">
          <button className={deviceMode === 'mobile' ? 'active' : ''} onClick={() => setDeviceMode('mobile')}>📱</button>
          <button className={deviceMode === 'tablet' ? 'active' : ''} onClick={() => setDeviceMode('tablet')}>📲</button>
          <button className={deviceMode === 'desktop' ? 'active' : ''} onClick={() => setDeviceMode('desktop')}>💻</button>
        </div>
      </div>
      
      <div className="preview-stage">
        <div className={`device-frame ${deviceMode}`}>
          <iframe ref={iframeRef} title="Preview" />
        </div>
      </div>
    </div>
  )
}

export default PreviewV2