import { useState, useEffect } from 'react'

export default function AnimatedDialog({ isOpen, onClose, animation = 'fade', children }) {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    if (isOpen) {
      setIsVisible(true)
    }
  }, [isOpen])

  const handleClose = () => {
    setIsVisible(false)
    setTimeout(onClose, 300)
  }

  if (!isOpen) return null

  return (
    <>
      <div className={`dialog-overlay ${isVisible ? 'visible' : ''}`} onClick={handleClose} />
      <div className={`dialog animated-dialog animation-${animation} ${isVisible ? 'visible' : ''}`}>
        <button className="close-btn" onClick={handleClose}>×</button>
        <div className="dialog-content">{children}</div>
      </div>
    </>
  )
}