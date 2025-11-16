import { useEffect, useRef } from 'react'
import './Preview.css'

function Preview({ html }) {
  const iframeRef = useRef(null)

  useEffect(() => {
    if (iframeRef.current && html) {
      const iframe = iframeRef.current
      const document = iframe.contentDocument || iframe.contentWindow.document

      document.open()
      document.write(html)
      document.close()
    }
  }, [html])

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
      <div className="preview-content">
        {html ? (
          <iframe
            ref={iframeRef}
            title="Website Preview"
            sandbox="allow-scripts allow-same-origin"
          />
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
