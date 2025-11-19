import { useState, useRef, useEffect } from 'react'

export default function Dropdown({ label = '{{DROPDOWN_LABEL}}', options = [] }) {
  const [isOpen, setIsOpen] = useState(false)
  const [selected, setSelected] = useState(null)
  const dropdownRef = useRef(null)

  const defaultOptions = [
    { value: '1', label: '{{OPTION_1}}' },
    { value: '2', label: '{{OPTION_2}}' },
    { value: '3', label: '{{OPTION_3}}' }
  ]

  const items = options.length > 0 ? options : defaultOptions

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
    <div className="dropdown" ref={dropdownRef}>
      <button className="dropdown-trigger" onClick={() => setIsOpen(!isOpen)}>
        {selected ? selected.label : label}
        <span className="dropdown-arrow">{isOpen ? '▲' : '▼'}</span>
      </button>
      {isOpen && (
        <div className="dropdown-menu">
          {items.map((option) => (
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
      )}
    </div>
  )
}