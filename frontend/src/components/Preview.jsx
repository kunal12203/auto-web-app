import { useEffect, useRef, useState } from 'react'
import './Preview.css' // Make sure you have the CSS from the previous step or use the inline styles below

function Preview({ files, selectedFile, onConsoleError }) {
  const iframeRef = useRef(null)
  const [deviceMode, setDeviceMode] = useState('desktop')
  const [isLoading, setIsLoading] = useState(true)

  // Helper to find the entry point
  const getEntryHtml = () => {
    if (!files) return ''
    // Look for index.html, main.html, or the first HTML file
    const entry = Object.keys(files).find(f => f === 'index.html' || f === 'main.html' || f.endsWith('.html'))
    if (!entry) return '<div style="color:white; padding:20px; font-family:sans-serif;"><h1>No HTML file found</h1><p>The AI generated code, but no entry HTML file was detected.</p></div>'
    return files[entry]
  }

  // Inject CSS/JS into the HTML for preview
  const processHtml = (rawHtml) => {
    if (!rawHtml) return ''
    
    let processed = rawHtml

    // Inject CSS
    const cssFiles = Object.keys(files).filter(f => f.endsWith('.css'))
    const styles = cssFiles.map(f => `<style>/* ${f} */\n${files[f]}</style>`).join('\n')
    processed = processed.replace('</head>', `${styles}\n</head>`)

    // Inject JS (Basic injection - complex modules might need a bundler in a real production env)
    const jsFiles = Object.keys(files).filter(f => f.endsWith('.js') && !f.includes('.test.'))
    const scripts = jsFiles.map(f => `<script>/* ${f} */\ntry{ ${files[f]} } catch(e) { console.error(e) }</script>`).join('\n')
    processed = processed.replace('</body>', `${scripts}\n</body>`)

    return processed
  }

  useEffect(() => {
    const rawHtml = getEntryHtml()
    const finalHtml = processHtml(rawHtml)

    if (iframeRef.current) {
      setIsLoading(true)
      const iframe = iframeRef.current
      const doc = iframe.contentDocument || iframe.contentWindow.document
      
      // Reset iframe
      doc.open()
      doc.write(finalHtml)
      doc.close()

      // Capture errors inside iframe
      iframe.contentWindow.onerror = (message, source, lineno, colno, error) => {
        if (onConsoleError) {
          onConsoleError({ message, source, lineno, colno })
        }
      }

      // Stop loading after a brief delay to allow render
      setTimeout(() => setIsLoading(false), 500)
    }
  }, [files, selectedFile])

  return (
    <div className="preview-container-glass">
      <div className="preview-toolbar">
        <div className="traffic-lights">
          <span className="light red"></span>
          <span className="light yellow"></span>
          <span className="light green"></span>
        </div>
        
        <div className="url-bar-glass">
          <span className="lock-icon">🔒</span>
          <span className="url-text">localhost:3000</span>
        </div>

        <div className="device-controls">
          <button 
            className={`device-btn ${deviceMode === 'mobile' ? 'active' : ''}`} 
            onClick={() => setDeviceMode('mobile')}
            title="Mobile View"
          >
            📱
          </button>
          <button 
            className={`device-btn ${deviceMode === 'tablet' ? 'active' : ''}`} 
            onClick={() => setDeviceMode('tablet')}
            title="Tablet View"
          >
            📲
          </button>
          <button 
            className={`device-btn ${deviceMode === 'desktop' ? 'active' : ''}`} 
            onClick={() => setDeviceMode('desktop')}
            title="Desktop View"
          >
            💻
          </button>
        </div>
      </div>

      <div className="preview-stage">
        <div className={`device-frame ${deviceMode}`}>
          {isLoading && (
            <div className="preview-loader">
              <div className="spinner"></div>
            </div>
          )}
          <iframe 
            ref={iframeRef} 
            title="Live Preview"
            sandbox="allow-scripts allow-modals allow-forms allow-same-origin"
          />
        </div>
      </div>
    </div>
  )
}

export default Preview