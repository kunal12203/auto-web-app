import { useState } from 'react'

export default function ResizableDialog({ isOpen, onClose, title, children }) {
  const [size, setSize] = useState({ width: 500, height: 400 })

  const handleResize = (e) => {
    const newWidth = e.clientX - e.target.offsetLeft
    const newHeight = e.clientY - e.target.offsetTop
    setSize({ width: Math.max(300, newWidth), height: Math.max(200, newHeight) })
  }

  if (!isOpen) return null

  return (
    <>
      <div className="dialog-overlay" onClick={onClose} />
      <div className="dialog resizable-dialog" style={{ width: size.width, height: size.height }}>
        <div className="dialog-header">
          <h2>{title}</h2>
          <button onClick={onClose}>×</button>
        </div>
        <div className="dialog-content">{children}</div>
        <div className="resize-handle" onMouseDown={handleResize} />
      </div>
    </>
  )
}