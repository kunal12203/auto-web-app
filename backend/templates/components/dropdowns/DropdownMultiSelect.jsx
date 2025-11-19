import { useState, useRef, useEffect } from 'react'

export default function MultiSelectDropdown({ label = 'Select items', options = [] }) {
  const [isOpen, setIsOpen] = useState(false)
  const [selected, setSelected] = useState([])
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

  const toggleOption = (option) => {
    setSelected(prev =>
      prev.find(item => item.value === option.value)
        ? prev.filter(item => item.value !== option.value)
        : [...prev, option]
    )
  }

  return (
    <div className="multi-select-dropdown" ref={dropdownRef}>
      <button className="dropdown-trigger" onClick={() => setIsOpen(!isOpen)}>
        {selected.length > 0 ? `${selected.length} selected` : label}
        <span className="dropdown-arrow">{isOpen ? '▲' : '▼'}</span>
      </button>
      {isOpen && (
        <div className="dropdown-menu">
          {options.map((option) => (
            <label key={option.value} className="dropdown-item checkbox-item">
              <input
                type="checkbox"
                checked={selected.find(item => item.value === option.value) !== undefined}
                onChange={() => toggleOption(option)}
              />
              <span>{option.label}</span>
            </label>
          ))}
        </div>
      )}
      {selected.length > 0 && (
        <div className="selected-tags">
          {selected.map((item) => (
            <span key={item.value} className="tag">
              {item.label}
              <button onClick={() => toggleOption(item)}>×</button>
            </span>
          ))}
        </div>
      )}
    </div>
  )
}