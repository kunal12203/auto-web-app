import { useEffect, useRef, useState } from 'react'
import './Preview.css'

function Preview({ html }) {
  const iframeRef = useRef(null)
  const [currentUrl, setCurrentUrl] = useState('about:blank')
  const [canGoBack, setCanGoBack] = useState(false)
  const [canGoForward, setCanGoForward] = useState(false)
  const [deviceMode, setDeviceMode] = useState('desktop') // desktop, tablet, mobile
  const [isRefreshing, setIsRefreshing] = useState(false)

  useEffect(() => {
    if (iframeRef.current && html) {
      const iframe = iframeRef.current
      const document = iframe.contentDocument || iframe.contentWindow.document

      document.open()
      document.write(html)
      document.close()

      setCurrentUrl('Generated Website')

      // Set up navigation event listeners
      const iframeWindow = iframe.contentWindow
      if (iframeWindow) {
        // Intercept all link clicks to prevent breaking out of iframe
        const interceptClicks = (e) => {
          const target = e.target.closest('a, button[onclick]')
          if (target) {
            // If it's a link with href
            if (target.tagName === 'A' && target.href) {
              const href = target.getAttribute('href')

              // Allow hash navigation
              if (href && href.startsWith('#')) {
                // Let it navigate normally within iframe
                return
              }

              // Prevent external navigation or target="_blank" links
              if (href && (href.startsWith('http') || target.target === '_blank' || target.target === '_top' || target.target === '_parent')) {
                e.preventDefault()
                console.log('Blocked external navigation:', href)

                // Show a message to user
                const message = document.createElement('div')
                message.textContent = 'External links are disabled in preview mode'
                message.style.cssText = 'position:fixed;top:20px;left:50%;transform:translateX(-50%);background:#f59e0b;color:white;padding:12px 24px;border-radius:8px;z-index:10000;font-family:system-ui;box-shadow:0 4px 12px rgba(0,0,0,0.15);'
                document.body.appendChild(message)
                setTimeout(() => message.remove(), 3000)
                return
              }
            }
          }
        }

        // Add click interceptor after a small delay to ensure DOM is ready
        setTimeout(() => {
          const iframeDoc = iframe.contentDocument || iframe.contentWindow.document
          iframeDoc.addEventListener('click', interceptClicks, true)
        }, 100)

        // Listen for navigation within the iframe
        const handleNavigation = () => {
          try {
            const href = iframeWindow.location.href
            if (href && href !== 'about:blank') {
              setCurrentUrl(href)
            }
          } catch (e) {
            // Cross-origin restrictions
            setCurrentUrl('Generated Website')
          }
        }

        // Monitor navigation state
        const checkNavigationState = () => {
          try {
            setCanGoBack(iframeWindow.history.length > 1)
            setCanGoForward(false) // Limited access to forward history
          } catch (e) {
            // Ignore errors
          }
        }

        iframeWindow.addEventListener('load', handleNavigation)
        iframeWindow.addEventListener('hashchange', handleNavigation)

        const interval = setInterval(checkNavigationState, 500)

        return () => {
          const iframeDoc = iframe.contentDocument || iframe.contentWindow.document
          if (iframeDoc) {
            iframeDoc.removeEventListener('click', interceptClicks, true)
          }
          iframeWindow.removeEventListener('load', handleNavigation)
          iframeWindow.removeEventListener('hashchange', handleNavigation)
          clearInterval(interval)
        }
      }
    }
  }, [html])

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
    if (iframeRef.current && html) {
      setIsRefreshing(true)
      const iframe = iframeRef.current
      const document = iframe.contentDocument || iframe.contentWindow.document

      document.open()
      document.write(html)
      document.close()

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

      {html && (
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
            </div>
          </div>
        </>
      )}

      <div className="preview-content">
        {html ? (
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
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                <line x1="8" y1="21" x2="16" y2="21"></line>
                <line x1="12" y1="17" x2="12" y2="21"></line>
              </svg>
              <h3>No website generated yet</h3>
              <p>Enter a prompt and click "Generate Website" to see your creation come to life!</p>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default Preview
