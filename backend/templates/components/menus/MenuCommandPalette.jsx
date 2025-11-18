import { useState, useEffect, useRef } from 'react'

export default function CommandPalette({ commands = [], isOpen, onClose }) {
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedIndex, setSelectedIndex] = useState(0)
  const inputRef = useRef(null)

  const filteredCommands = commands.filter(cmd =>
    cmd.label.toLowerCase().includes(searchTerm.toLowerCase()) ||
    cmd.keywords?.some(k => k.toLowerCase().includes(searchTerm.toLowerCase()))
  )

  useEffect(() => {
    if (isOpen) {
      inputRef.current?.focus()
    }
  }, [isOpen])

  const handleKeyDown = (e) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault()
      setSelectedIndex((prev) => Math.min(prev + 1, filteredCommands.length - 1))
    } else if (e.key === 'ArrowUp') {
      e.preventDefault()
      setSelectedIndex((prev) => Math.max(prev - 1, 0))
    } else if (e.key === 'Enter') {
      e.preventDefault()
      filteredCommands[selectedIndex]?.action()
      onClose()
    } else if (e.key === 'Escape') {
      onClose()
    }
  }

  if (!isOpen) return null

  return (
    <>
      <div className="command-palette-overlay" onClick={onClose} />
      <div className="command-palette">
        <input
          ref={inputRef}
          type="text"
          placeholder="Type a command..."
          value={searchTerm}
          onChange={(e) => {
            setSearchTerm(e.target.value)
            setSelectedIndex(0)
          }}
          onKeyDown={handleKeyDown}
        />
        <div className="command-list">
          {filteredCommands.map((cmd, index) => (
            <button
              key={index}
              className={`command-item ${index === selectedIndex ? 'selected' : ''}`}
              onClick={() => {
                cmd.action()
                onClose()
              }}
            >
              {cmd.icon && <span className="command-icon">{cmd.icon}</span>}
              <div className="command-content">
                <span className="command-label">{cmd.label}</span>
                {cmd.description && <span className="command-description">{cmd.description}</span>}
              </div>
              {cmd.shortcut && <span className="command-shortcut">{cmd.shortcut}</span>}
            </button>
          ))}
        </div>
      </div>
    </>
  )
}