import './StatusBar.css'

function StatusBar({ status, message }) {
  return (
    <div className={`status-bar-container ${status}`}>
      <div className="status-pulse"></div>
      <div className="status-text">
        <span className="status-label">SYSTEM STATUS:</span>
        <span className="status-message">{message}</span>
      </div>
      <div className="status-decoration">
        <span></span><span></span><span></span>
      </div>
    </div>
  )
}

export default StatusBar