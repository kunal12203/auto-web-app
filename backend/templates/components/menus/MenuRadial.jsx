import { useState } from 'react'

export default function RadialMenu({ items = [], centerIcon = '☰' }) {
  const [isOpen, setIsOpen] = useState(false)

  const getItemPosition = (index, total) => {
    const angle = (360 / total) * index - 90
    const radius = 100
    const x = Math.cos(angle * Math.PI / 180) * radius
    const y = Math.sin(angle * Math.PI / 180) * radius
    return { x, y }
  }

  return (
    <div className="radial-menu-container">
      <button className="radial-menu-center" onClick={() => setIsOpen(!isOpen)}>
        {centerIcon}
      </button>
      {isOpen && (
        <div className="radial-menu">
          {items.map((item, index) => {
            const pos = getItemPosition(index, items.length)
            return (
              <button
                key={index}
                className="radial-menu-item"
                style={{ transform: `translate(${pos.x}px, ${pos.y}px)` }}
                onClick={item.onClick}
              >
                {item.icon || item.label}
              </button>
            )
          })}
        </div>
      )}
    </div>
  )
}