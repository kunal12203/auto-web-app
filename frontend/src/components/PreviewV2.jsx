import { useEffect, useRef, useState } from 'react'
import './Preview.css'

function PreviewV2({ files, projectType, onConsoleError }) {
  const iframeRef = useRef(null)
  const [currentUrl, setCurrentUrl] = useState('about:blank')
  const [canGoBack, setCanGoBack] = useState(false)
  const [canGoForward, setCanGoForward] = useState(false)
  const [deviceMode, setDeviceMode] = useState('desktop')
  const [isRefreshing, setIsRefreshing] = useState(false)
  const [consoleErrors, setConsoleErrors] = useState([])
  const [showConsole, setShowConsole] = useState(false)

  // Generate preview HTML from project files
  const generatePreviewHTML = (files) => {
    if (!files || Object.keys(files).length === 0) {
      return null
    }

    // For simple HTML projects
    if (files['index.html']) {
      let html = files['index.html']

      // Inject inline CSS if exists
      if (files['styles.css']) {
        html = html.replace(
          '<link rel="stylesheet" href="styles.css">',
          `<style>${files['styles.css']}</style>`
        )
      }

      // Inject inline JS if exists
      if (files['script.js']) {
        html = html.replace(
          '<script src="script.js"></script>',
          `<script>${files['script.js']}</script>`
        )
      }

      return html
    }

    // For React projects - generate a simple preview HTML
    if (files['src/App.jsx']) {
      // Note: For real React preview, we'd need to bundle it
      // For now, show a message that React preview requires build
      return `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>React Project Preview</title>
  <style>
    body {
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
        'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      text-align: center;
      padding: 20px;
    }
    .preview-info {
      max-width: 600px;
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(10px);
      padding: 40px;
      border-radius: 16px;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    h1 { margin: 0 0 20px; }
    p { margin: 10px 0; opacity: 0.9; }
    .file-list {
      margin-top: 20px;
      padding: 20px;
      background: rgba(0, 0, 0, 0.2);
      border-radius: 8px;
      text-align: left;
    }
    .file-item {
      padding: 8px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .file-item:last-child {
      border-bottom: none;
    }
    code {
      background: rgba(0, 0, 0, 0.3);
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 14px;
    }
  </style>
</head>
<body>
  <div class="preview-info">
    <h1>🚀 React Project Generated</h1>
    <p>Your React project has been successfully scaffolded!</p>
    <p>To run this project:</p>
    <div class="file-list">
      <code>1. Extract the exported ZIP file</code><br/><br/>
      <code>2. cd project-folder</code><br/><br/>
      <code>3. npm install</code><br/><br/>
      <code>4. npm run dev</code>
    </div>
    <p style="margin-top: 20px; font-size: 14px;">
      Export your project to get all files including:<br/>
      ${Object.keys(files).slice(0, 5).join(', ')}...
    </p>
  </div>
</body>
</html>
`
    }

    return null
  }

  useEffect(() => {
    const html = generatePreviewHTML(files)

    if (iframeRef.current && html) {
      const iframe = iframeRef.current
      const iframeDoc = iframe.contentDocument || iframe.contentWindow.document
      const iframeWin = iframe.contentWindow

      iframeDoc.open()
      iframeDoc.write(html)
      iframeDoc.close()

      setCurrentUrl('Generated Website')

      // Capture console errors from iframe
      const originalConsoleError = iframeWin.console.error
      const originalConsoleWarn = iframeWin.console.warn
      const capturedErrors = []

      iframeWin.console.error = function(...args) {
        const errorMsg = args.join(' ')
        const errorObj = {
          type: 'error',
          message: errorMsg,
          timestamp: new Date().toISOString(),
          stack: new Error().stack
        }

        capturedErrors.push(errorObj)
        setConsoleErrors(prev => [...prev, errorObj])

        // Send to parent for AI fixing
        if (onConsoleError) {
          onConsoleError(errorObj)
        }

        originalConsoleError.apply(iframeWin.console, args)
      }

      iframeWin.console.warn = function(...args) {
        const warnMsg = args.join(' ')
        const warnObj = {
          type: 'warning',
          message: warnMsg,
          timestamp: new Date().toISOString()
        }

        capturedErrors.push(warnObj)
        setConsoleErrors(prev => [...prev, warnObj])

        originalConsoleWarn.apply(iframeWin.console, args)
      }

      // Capture uncaught errors
      iframeWin.addEventListener('error', (event) => {
        const errorObj = {
          type: 'error',
          message: event.message || 'Uncaught error',
          filename: event.filename,
          lineno: event.lineno,
          colno: event.colno,
          timestamp: new Date().toISOString()
        }

        capturedErrors.push(errorObj)
        setConsoleErrors(prev => [...prev, errorObj])

        if (onConsoleError) {
          onConsoleError(errorObj)
        }
      })

      // Intercept clicks to prevent navigation issues
      setTimeout(() => {
        const doc = iframe.contentDocument || iframe.contentWindow.document
        doc.addEventListener('click', (e) => {
          const target = e.target.closest('a')
          if (target && target.href) {
            const href = target.getAttribute('href')
            if (href && !href.startsWith('#') && (href.startsWith('http') || target.target === '_blank')) {
              e.preventDefault()
              console.log('Blocked external navigation:', href)
            }
          }
        }, true)
      }, 100)

      // Navigation listeners
      const handleNavigation = () => {
        try {
          const href = iframeWin.location.href
          if (href && href !== 'about:blank') {
            setCurrentUrl(href)
          }
        } catch (e) {
          setCurrentUrl('Generated Website')
        }
      }

      const checkNavigationState = () => {
        try {
          setCanGoBack(iframeWin.history.length > 1)
          setCanGoForward(false)
        } catch (e) {
          // Ignore
        }
      }

      iframeWin.addEventListener('load', handleNavigation)
      iframeWin.addEventListener('hashchange', handleNavigation)
      const interval = setInterval(checkNavigationState, 500)

      return () => {
        iframeWin.console.error = originalConsoleError
        iframeWin.console.warn = originalConsoleWarn
        iframeWin.removeEventListener('load', handleNavigation)
        iframeWin.removeEventListener('hashchange', handleNavigation)
        clearInterval(interval)
      }
    }
  }, [files, onConsoleError])

  const handleBack = () => {
    if (iframeRef.current && canGoBack) {
      try {
        iframeRef.current.contentWindow.history.back()
      } catch (e) {
        console.error('Navigation error:', e)
      }
    }
  }

  const handleForward = () => {
    if (iframeRef.current && canGoForward) {
      try {
        iframeRef.current.contentWindow.history.forward()
      } catch (e) {
        console.error('Navigation error:', e)
      }
    }
  }

  const handleRefresh = () => {
    const html = generatePreviewHTML(files)
    if (iframeRef.current && html) {
      setIsRefreshing(true)
      const iframe = iframeRef.current
      const document = iframe.contentDocument || iframe.contentWindow.document

      document.open()
      document.write(html)
      document.close()

      // Clear console errors on refresh
      setConsoleErrors([])

      setTimeout(() => setIsRefreshing(false), 500)
    }
  }

  const getDeviceClass = () => {
    switch (deviceMode) {
      case 'mobile':
        return 'device-mobile'
      case 'tablet':
        return 'device-tablet'
      default:
        return 'device-desktop'
    }
  }

  const hasContent = files && Object.keys(files).length > 0

  return (
    <div className="preview-container">
      <div className="preview-header">
        <h2>Live Preview</h2>
        <div className="preview-controls">
          <span className="preview-dot" style={{ background: '#ff5f56' }}></span>
          <span className="preview-dot" style={{ background: '#ffbd2e' }}></span>
          <span className="preview-dot" style={{ background: '#27c93f' }}></span>
        </div>
      </div>

      {hasContent && (
        <>
          <div className="preview-toolbar">
            <div className="navigation-controls">
              <button
                className="nav-btn"
                onClick={handleBack}
                disabled={!canGoBack}
                title="Go back"
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <polyline points="15 18 9 12 15 6"></polyline>
                </svg>
              </button>
              <button
                className="nav-btn"
                onClick={handleForward}
                disabled={!canGoForward}
                title="Go forward"
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
              </button>
              <button
                className={`nav-btn ${isRefreshing ? 'refreshing' : ''}`}
                onClick={handleRefresh}
                title="Refresh"
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <polyline points="23 4 23 10 17 10"></polyline>
                  <polyline points="1 20 1 14 7 14"></polyline>
                  <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
                </svg>
              </button>
            </div>

            <div className="url-bar">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="2" y1="12" x2="22" y2="12"></line>
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
              </svg>
              <span className="url-text">{currentUrl}</span>
            </div>

            <div className="device-controls">
              <button
                className={`device-btn ${deviceMode === 'desktop' ? 'active' : ''}`}
                onClick={() => setDeviceMode('desktop')}
                title="Desktop view"
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                  <line x1="8" y1="21" x2="16" y2="21"></line>
                  <line x1="12" y1="17" x2="12" y2="21"></line>
                </svg>
              </button>
              <button
                className={`device-btn ${deviceMode === 'tablet' ? 'active' : ''}`}
                onClick={() => setDeviceMode('tablet')}
                title="Tablet view"
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect>
                  <line x1="12" y1="18" x2="12.01" y2="18"></line>
                </svg>
              </button>
              <button
                className={`device-btn ${deviceMode === 'mobile' ? 'active' : ''}`}
                onClick={() => setDeviceMode('mobile')}
                title="Mobile view"
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <rect x="7" y="2" width="10" height="20" rx="2" ry="2"></rect>
                  <line x1="12" y1="18" x2="12.01" y2="18"></line>
                </svg>
              </button>

              {consoleErrors.length > 0 && (
                <button
                  className={`device-btn console-btn ${showConsole ? 'active' : ''}`}
                  onClick={() => setShowConsole(!showConsole)}
                  title={`Console (${consoleErrors.length} ${consoleErrors.length === 1 ? 'error' : 'errors'})`}
                >
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <polyline points="4 17 10 11 4 5"></polyline>
                    <line x1="12" y1="19" x2="20" y2="19"></line>
                  </svg>
                  <span className="error-badge">{consoleErrors.length}</span>
                </button>
              )}
            </div>
          </div>

          {showConsole && consoleErrors.length > 0 && (
            <div className="console-panel">
              <div className="console-header">
                <span>Console Output</span>
                <button onClick={() => setConsoleErrors([])}>Clear</button>
              </div>
              <div className="console-content">
                {consoleErrors.map((error, index) => (
                  <div key={index} className={`console-item console-${error.type}`}>
                    <span className="console-type">{error.type === 'error' ? '❌' : '⚠️'}</span>
                    <span className="console-message">{error.message}</span>
                    <span className="console-time">
                      {new Date(error.timestamp).toLocaleTimeString()}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </>
      )}

      <div className="preview-content">
        {hasContent ? (
          <div className={`iframe-wrapper ${getDeviceClass()}`}>
            <iframe
              ref={iframeRef}
              title="Website Preview"
              sandbox="allow-scripts allow-same-origin allow-forms allow-modals"
            />
          </div>
        ) : (
          <div className="preview-placeholder">
            <div className="placeholder-content">
              <svg
                width="120"
                height="120"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.5"
              >
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                <line x1="8" y1="21" x2="16" y2="21"></line>
                <line x1="12" y1="17" x2="12" y2="21"></line>
              </svg>
              <h3>No website generated yet</h3>
              <p>Enter a prompt and click "Generate Website" to see your creation!</p>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default PreviewV2
