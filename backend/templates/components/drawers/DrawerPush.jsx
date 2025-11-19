export default function PushDrawer({ isOpen, onClose, children }) {
  return (
    <div className={`push-drawer-container ${isOpen ? 'drawer-open' : ''}`}>
      <div className="drawer drawer-push">
        <button className="drawer-close" onClick={onClose}>×</button>
        <div className="drawer-content">{children}</div>
      </div>
      <div className="main-content">
        <button onClick={() => !isOpen && onClose()}>☰</button>
        {/* Main content */}
      </div>
    </div>
  )
}