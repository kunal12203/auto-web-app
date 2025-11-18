import { useState, useRef, useEffect } from 'react'

export default function SearchableDropdown({ label = 'Search...', options = [] }) {
  const [isOpen, setIsOpen] = useState(false)
  const [searchTerm, setSearchTerm] = useState('')
  const [selected, setSelected] = useState(null)
  const dropdownRef = useRef(null)

  const filteredOptions = options.filter(option =>
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

  return (
    <div className="searchable-dropdown" ref={dropdownRef}>
      <div className="dropdown-trigger">
        <input
          type="text"
          placeholder={selected ? selected.label : label}
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          onFocus={() => setIsOpen(true)}
        />
      </div>
      {isOpen && (
        <div className="dropdown-menu">
          {filteredOptions.length > 0 ? (
            filteredOptions.map((option) => (
              <button
                key={option.value}
                className="dropdown-item"
                onClick={() => {
                  setSelected(option)
                  setSearchTerm('')
                  setIsOpen(false)
                }}
              >
                {option.label}
              </button>
            ))
          ) : (
            <div className="dropdown-item no-results">No results found</div>
          )}
        </div>
      )}
    </div>
  )
}