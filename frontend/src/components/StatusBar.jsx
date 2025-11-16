import './StatusBar.css'

function StatusBar({ status, message }) {
  const getStatusIcon = () => {
    switch (status) {
      case 'connected':
        return '✓'
      case 'generating':
        return '⟳'
      case 'success':
        return '✓'
      case 'error':
        return '✗'
      case 'disconnected':
        return '⊗'
      default:
        return '○'
    }
  }

  return (
    <div className={`status-bar status-${status}`}>
      <span className="status-icon">{getStatusIcon()}</span>
      <span className="status-message">{message}</span>
    </div>
  )
}

export default StatusBar
