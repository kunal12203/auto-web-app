import { useState, useRef, useEffect } from 'react'

export default function AdvancedDropdownMenu({ trigger, items = [] }) {
  const [isOpen, setIsOpen] = useState(false)
  const menuRef = useRef(null)

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (menuRef.current && !menuRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  return (
    <div className="dropdown-menu-container" ref={menuRef}>
      <div onClick={() => setIsOpen(!isOpen)}>{trigger}</div>
      {isOpen && (
        <div className="dropdown-menu advanced">
          {items.map((item, index) => (
            <div key={index}>
              {item.divider ? (
                <div className="menu-divider" />
              ) : (
                <button
                  className={`menu-item ${item.danger ? 'danger' : ''} ${item.disabled ? 'disabled' : ''}`}
                  onClick={() => {
                    if (!item.disabled) {
                      item.onClick?.()
                      setIsOpen(false)
                    }
                  }}
                  disabled={item.disabled}
                >
                  {item.icon && <span className="menu-icon">{item.icon}</span>}
                  <div className="menu-item-content">
                    <span className="menu-label">{item.label}</span>
                    {item.description && <span className="menu-description">{item.description}</span>}
                  </div>
                  {item.shortcut && <span className="menu-shortcut">{item.shortcut}</span>}
                </button>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}