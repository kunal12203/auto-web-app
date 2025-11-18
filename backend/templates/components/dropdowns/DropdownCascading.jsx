import { useState, useRef, useEffect } from 'react'

export default function CascadingDropdown({ levels = [] }) {
  const [selectedPath, setSelectedPath] = useState([])
  const [isOpen, setIsOpen] = useState(false)
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

  const handleSelect = (levelIndex, option) => {
    const newPath = [...selectedPath.slice(0, levelIndex), option]
    setSelectedPath(newPath)

    if (!option.children || option.children.length === 0) {
      setIsOpen(false)
    }
  }

  const getOptions = (levelIndex) => {
    if (levelIndex === 0) return levels[0].options
    const parent = selectedPath[levelIndex - 1]
    return parent?.children || []
  }

  return (
    <div className="cascading-dropdown" ref={dropdownRef}>
      <button className="dropdown-trigger" onClick={() => setIsOpen(!isOpen)}>
        {selectedPath.length > 0 ? selectedPath.map(s => s.label).join(' > ') : 'Select...'}
      </button>
      {isOpen && (
        <div className="dropdown-menu cascading">
          {levels.map((level, levelIndex) => {
            const options = getOptions(levelIndex)
            if (!options || options.length === 0) return null

            return (
              <div key={levelIndex} className="dropdown-level">
                <div className="level-title">{level.label}</div>
                {options.map((option) => (
                  <button
                    key={option.value}
                    className={`dropdown-item ${selectedPath[levelIndex]?.value === option.value ? 'selected' : ''}`}
                    onClick={() => handleSelect(levelIndex, option)}
                  >
                    {option.label}
                    {option.children && option.children.length > 0 && <span> ›</span>}
                  </button>
                ))}
              </div>
            )
          })}
        </div>
      )}
    </div>
  )
}