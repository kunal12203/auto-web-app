import { useState, useRef, useEffect } from 'react'

export default function ContextMenu({ items = [] }) {
  const [isOpen, setIsOpen] = useState(false)
  const [position, setPosition] = useState({ x: 0, y: 0 })
  const menuRef = useRef(null)

  const handleContextMenu = (e) => {
    e.preventDefault()
    setPosition({ x: e.pageX, y: e.pageY })
    setIsOpen(true)
  }

  useEffect(() => {
    const handleClick = () => setIsOpen(false)
    if (isOpen) {
      document.addEventListener('click', handleClick)
    }
    return () => document.removeEventListener('click', handleClick)
  }, [isOpen])

  return (
    <div onContextMenu={handleContextMenu}>
      <div className="context-menu-target">Right click here</div>
      {isOpen && (
        <div
          ref={menuRef}
          className="context-menu"
          style={{ left: position.x, top: position.y }}
        >
          {items.map((item, index) => (
            <button key={index} className="menu-item" onClick={item.onClick}>
              {item.icon && <span className="menu-icon">{item.icon}</span>}
              {item.label}
            </button>
          ))}
        </div>
      )}
    </div>
  )
}