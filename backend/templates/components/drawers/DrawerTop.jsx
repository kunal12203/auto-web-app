import { useEffect } from 'react'

export default function TopDrawer({ isOpen, onClose, children }) {
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden'
    } else {
      document.body.style.overflow = 'unset'
    }
  }, [isOpen])

  return (
    <>
      {isOpen && <div className="drawer-overlay" onClick={onClose} />}
      <div className={`drawer drawer-top ${isOpen ? 'open' : ''}`}>
        <button className="drawer-close" onClick={onClose}>×</button>
        <div className="drawer-content">{children}</div>
      </div>
    </>
  )
}