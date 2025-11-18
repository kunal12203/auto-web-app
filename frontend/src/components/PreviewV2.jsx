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

  // Helper function to normalize paths
  const normalizePath = (path) => {
    return path.replace(/\\/g, '/').replace(/^\.\//, '')
  }

  // Helper function to resolve relative paths
  const resolvePath = (basePath, relativePath) => {
    if (relativePath.startsWith('http://') || relativePath.startsWith('https://') || relativePath.startsWith('data:')) {
      return relativePath
    }

    const baseDir = basePath.split('/').slice(0, -1).join('/')
    const parts = (baseDir ? baseDir + '/' + relativePath : relativePath).split('/')
    const resolved = []

    for (const part of parts) {
      if (part === '..') {
        resolved.pop()
      } else if (part !== '.' && part !== '') {
        resolved.push(part)
      }
    }

    return resolved.join('/')
  }

  // Find the main HTML file
  const findMainHTML = (files) => {
    const htmlFiles = Object.keys(files).filter(f => f.endsWith('.html'))

    // Priority order for finding the main HTML file
    const priorities = [
      'index.html',
      'main.html',
      'home.html',
      'public/index.html',
      'dist/index.html',
      'build/index.html'
    ]

    for (const priority of priorities) {
      if (files[priority]) return priority
    }

    // Find any HTML file in root
    const rootHTML = htmlFiles.find(f => !f.includes('/'))
    if (rootHTML) return rootHTML

    // Return first HTML file found
    return htmlFiles[0] || null
  }

  // Convert file to data URL
  const getFileDataURL = (filePath, files) => {
    const content = files[filePath]
    if (!content) return null

    const extension = filePath.split('.').pop().toLowerCase()
    const mimeTypes = {
      'css': 'text/css',
      'js': 'application/javascript',
      'json': 'application/json',
      'png': 'image/png',
      'jpg': 'image/jpeg',
      'jpeg': 'image/jpeg',
      'gif': 'image/gif',
      'svg': 'image/svg+xml',
      'webp': 'image/webp',
      'ico': 'image/x-icon',
      'woff': 'font/woff',
      'woff2': 'font/woff2',
      'ttf': 'font/ttf',
      'eot': 'application/vnd.ms-fontobject'
    }

    const mimeType = mimeTypes[extension] || 'text/plain'

    // For text files, encode as UTF-8
    if (mimeType.startsWith('text/') || mimeType.includes('javascript') || mimeType.includes('json') || extension === 'svg') {
      return `data:${mimeType};charset=utf-8,${encodeURIComponent(content)}`
    }

    // For binary files, assume base64 if it looks like base64, otherwise encode as text
    if (content.match(/^[A-Za-z0-9+/]+=*$/)) {
      return `data:${mimeType};base64,${content}`
    }

    return `data:${mimeType};charset=utf-8,${encodeURIComponent(content)}`
  }

  // Process CSS to resolve imports and URLs
  const processCSS = (css, cssPath, files) => {
    if (!css) return ''

    // Replace @import statements
    css = css.replace(/@import\s+(?:url\()?['"]([^'"]+)['"](?:\))?[^;]*;/g, (match, importPath) => {
      const resolvedPath = resolvePath(cssPath, importPath)
      const importedCSS = files[resolvedPath]
      if (importedCSS) {
        return processCSS(importedCSS, resolvedPath, files)
      }
      return match
    })

    // Replace url() references
    css = css.replace(/url\(['"]?([^'")]+)['"]?\)/g, (match, urlPath) => {
      if (urlPath.startsWith('data:') || urlPath.startsWith('http')) {
        return match
      }
      const resolvedPath = resolvePath(cssPath, urlPath)
      const dataURL = getFileDataURL(resolvedPath, files)
      return dataURL ? `url('${dataURL}')` : match
    })

    return css
  }

  // Generate preview HTML from project files
  const generatePreviewHTML = (files) => {
    if (!files || Object.keys(files).length === 0) {
      return null
    }

    // Check if this is a React/Vue/Angular project
    const isReactProject = files['src/App.jsx'] || files['src/App.tsx'] || files['package.json']?.includes('react')
    const isVueProject = files['src/App.vue'] || files['package.json']?.includes('vue')
    const isAngularProject = files['angular.json'] || files['package.json']?.includes('@angular')

    if (isReactProject || isVueProject || isAngularProject) {
      const projectType = isReactProject ? 'React' : isVueProject ? 'Vue' : 'Angular'
      return `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${projectType} Project Preview</title>
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
    <h1>🚀 ${projectType} Project Generated</h1>
    <p>Your ${projectType} project has been successfully scaffolded!</p>
    <p>To run this project:</p>
    <div class="file-list">
      <code>1. Export the ZIP file</code><br/><br/>
      <code>2. Extract and cd into the folder</code><br/><br/>
      <code>3. npm install</code><br/><br/>
      <code>4. npm run dev</code>
    </div>
    <p style="margin-top: 20px; font-size: 14px;">
      Project includes ${Object.keys(files).length} files
    </p>
  </div>
</body>
</html>
`
    }

    // Find the main HTML file
    const mainHTMLPath = findMainHTML(files)
    if (!mainHTMLPath) {
      return null
    }

    let html = files[mainHTMLPath]

    // Process and inline CSS files
    html = html.replace(/<link\s+([^>]*href=['"]([^'"]+\.css)['"][^>]*)>/gi, (match, attrs, href) => {
      const resolvedPath = resolvePath(mainHTMLPath, href)
      const cssContent = files[resolvedPath]

      if (cssContent) {
        const processedCSS = processCSS(cssContent, resolvedPath, files)
        return `<style>${processedCSS}</style>`
      }
      return match
    })

    // Process and inline JavaScript files
    html = html.replace(/<script\s+([^>]*src=['"]([^'"]+\.js)['"][^>]*)><\/script>/gi, (match, attrs, src) => {
      // Skip external scripts
      if (src.startsWith('http://') || src.startsWith('https://')) {
        return match
      }

      const resolvedPath = resolvePath(mainHTMLPath, src)
      const jsContent = files[resolvedPath]

      if (jsContent) {
        // Check if it's a module script
        const isModule = attrs.includes('type="module"') || attrs.includes("type='module'")
        return isModule
          ? `<script type="module">${jsContent}</script>`
          : `<script>${jsContent}</script>`
      }
      return match
    })

    // Process image sources
    html = html.replace(/<img\s+([^>]*src=['"]([^'"]+)['"][^>]*)>/gi, (match, attrs, src) => {
      if (src.startsWith('http://') || src.startsWith('https://') || src.startsWith('data:')) {
        return match
      }

      const resolvedPath = resolvePath(mainHTMLPath, src)
      const dataURL = getFileDataURL(resolvedPath, files)

      if (dataURL) {
        return match.replace(src, dataURL)
      }
      return match
    })

    // Process inline style background images
    html = html.replace(/style=['"]([^'"]*background(?:-image)?:[^'"]*url\(([^)]+)\)[^'"]*)['"]'/gi, (match, style, url) => {
      const cleanUrl = url.replace(/['"]/g, '')
      if (cleanUrl.startsWith('http://') || cleanUrl.startsWith('https://') || cleanUrl.startsWith('data:')) {
        return match
      }

      const resolvedPath = resolvePath(mainHTMLPath, cleanUrl)
      const dataURL = getFileDataURL(resolvedPath, files)

      if (dataURL) {
        return match.replace(url, `'${dataURL}'`)
      }
      return match
    })

    return html
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
