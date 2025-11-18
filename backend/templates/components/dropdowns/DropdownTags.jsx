import { useState, useRef, useEffect } from 'react'

export default function TagsDropdown({ options = [], placeholder = 'Add tags...' }) {
  const [isOpen, setIsOpen] = useState(false)
  const [searchTerm, setSearchTerm] = useState('')
  const [selected, setSelected] = useState([])
  const dropdownRef = useRef(null)
  const inputRef = useRef(null)

  const filteredOptions = options.filter(option =>
    !selected.find(s => s.value === option.value) &&
    option.label.toLowerCase().includes(searchTerm.toLowerCase())
  )

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  const addTag = (option) => {
    setSelected([...selected, option])
    setSearchTerm('')
    inputRef.current?.focus()
  }

  const removeTag = (option) => {
    setSelected(selected.filter(s => s.value !== option.value))
  }

  return (
    <div className="tags-dropdown" ref={dropdownRef}>
      <div className="tags-input-container">
        {selected.map((tag) => (
          <span key={tag.value} className="tag">
            {tag.label}
            <button onClick={() => removeTag(tag)}>×</button>
          </span>
        ))}
        <input
          ref={inputRef}
          type="text"
          placeholder={selected.length === 0 ? placeholder : ''}
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          onFocus={() => setIsOpen(true)}
        />
      </div>
      {isOpen && filteredOptions.length > 0 && (
        <div className="dropdown-menu">
          {filteredOptions.map((option) => (
            <button
              key={option.value}
              className="dropdown-item"
              onClick={() => addTag(option)}
            >
              {option.label}
            </button>
          ))}
        </div>
      )}
    </div>
  )
}