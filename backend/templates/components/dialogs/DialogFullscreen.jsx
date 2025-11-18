export default function FullscreenDialog({ isOpen, onClose, children }) {
  if (!isOpen) return null

  return (
    <div className="dialog fullscreen-dialog">
      <div className="dialog-header">
        <button className="close-btn" onClick={onClose}>×</button>
      </div>
      <div className="dialog-content">{children}</div>
    </div>
  )
}