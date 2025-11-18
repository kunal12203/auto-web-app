import { useEffect } from 'react'

export default function ScrollLockDialog({ isOpen, onClose, children }) {
  useEffect(() => {
    if (isOpen) {
      const scrollY = window.scrollY
      document.body.style.position = 'fixed'
      document.body.style.top = `-${scrollY}px`
      document.body.style.width = '100%'

      return () => {
        document.body.style.position = ''
        document.body.style.top = ''
        document.body.style.width = ''
        window.scrollTo(0, scrollY)
      }
    }
  }, [isOpen])

  if (!isOpen) return null

  return (
    <>
      <div className="dialog-overlay" onClick={onClose} />
      <div className="dialog scroll-lock-dialog">
        <button className="close-btn" onClick={onClose}>×</button>
        <div className="dialog-content">{children}</div>
      </div>
    </>
  )
}