import { useState, useRef, useEffect } from 'react'

export default function AsyncDropdown({ label = 'Search...', fetchOptions }) {
  const [isOpen, setIsOpen] = useState(false)
  const [searchTerm, setSearchTerm] = useState('')
  const [options, setOptions] = useState([])
  const [loading, setLoading] = useState(false)
  const [selected, setSelected] = useState(null)
  const dropdownRef = useRef(null)

  useEffect(() => {
    const loadOptions = async () => {
      if (searchTerm.length < 2) {
        setOptions([])
        return
      }

      setLoading(true)
      try {
        const results = await fetchOptions(searchTerm)
        setOptions(results)
      } catch (error) {
        console.error('Failed to fetch options:', error)
      }
      setLoading(false)
    }

    const debounceTimer = setTimeout(loadOptions, 300)
    return () => clearTimeout(debounceTimer)
  }, [searchTerm, fetchOptions])

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
    <div className="async-dropdown" ref={dropdownRef}>
      <input
        type="text"
        placeholder={selected ? selected.label : label}
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        onFocus={() => setIsOpen(true)}
      />
      {isOpen && (
        <div className="dropdown-menu">
          {loading && <div className="dropdown-item">Loading...</div>}
          {!loading && options.length === 0 && searchTerm.length >= 2 && (
            <div className="dropdown-item">No results found</div>
          )}
          {!loading && options.map((option) => (
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
          ))}
        </div>
      )}
    </div>
  )
}