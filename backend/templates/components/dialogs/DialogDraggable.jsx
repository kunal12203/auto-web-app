import { useState } from 'react'

export default function DraggableDialog({ isOpen, onClose, title, children }) {
  const [position, setPosition] = useState({ x: 0, y: 0 })
  const [isDragging, setIsDragging] = useState(false)
  const [dragStart, setDragStart] = useState({ x: 0, y: 0 })

  const handleMouseDown = (e) => {
    setIsDragging(true)
    setDragStart({ x: e.clientX - position.x, y: e.clientY - position.y })
  }

  const handleMouseMove = (e) => {
    if (!isDragging) return
    setPosition({ x: e.clientX - dragStart.x, y: e.clientY - dragStart.y })
  }

  const handleMouseUp = () => {
    setIsDragging(false)
  }

  if (!isOpen) return null

  return (
    <>
      <div className="dialog-overlay" onClick={onClose} />
      <div
        className="dialog draggable-dialog"
        style={{ transform: `translate(${position.x}px, ${position.y}px)` }}
        onMouseMove={handleMouseMove}
        onMouseUp={handleMouseUp}
      >
        <div className="dialog-header draggable-handle" onMouseDown={handleMouseDown}>
          <h2>{title}</h2>
          <button onClick={onClose}>×</button>
        </div>
        <div className="dialog-content">{children}</div>
      </div>
    </>
  )
}