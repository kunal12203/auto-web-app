import { useState, useRef, useEffect } from 'react'

export default function GroupedDropdown({ label = 'Select option', groups = [] }) {
  const [isOpen, setIsOpen] = useState(false)
  const [selected, setSelected] = useState(null)
  const dropdownRef = useRef(null)

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  return (
    <div className="grouped-dropdown" ref={dropdownRef}>
      <button className="dropdown-trigger" onClick={() => setIsOpen(!isOpen)}>
        {selected ? selected.label : label}
        <span>{isOpen ? '▲' : '▼'}</span>
      </button>
      {isOpen && (
        <div className="dropdown-menu">
          {groups.map((group, groupIndex) => (
            <div key={groupIndex} className="dropdown-group">
              <div className="group-label">{group.label}</div>
              {group.options.map((option) => (
                <button
                  key={option.value}
                  className="dropdown-item"
                  onClick={() => {
                    setSelected(option)
                    setIsOpen(false)
                  }}
                >
                  {option.label}
                </button>
              ))}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}