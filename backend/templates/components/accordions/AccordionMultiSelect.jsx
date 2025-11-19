import { useState } from 'react'

export default function MultiSelectAccordion({ items = [], allowMultiple = true }) {
  const [openIndexes, setOpenIndexes] = useState([])

  const toggleItem = (index) => {
    if (allowMultiple) {
      setOpenIndexes(prev =>
        prev.includes(index) ? prev.filter(i => i !== index) : [...prev, index]
      )
    } else {
      setOpenIndexes(prev => (prev.includes(index) ? [] : [index]))
    }
  }

  return (
    <div className="multi-select-accordion">
      {items.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header ${openIndexes.includes(index) ? 'active' : ''}`}
            onClick={() => toggleItem(index)}
          >
            {item.title}
            <span>{openIndexes.includes(index) ? '−' : '+'}</span>
          </button>
          {openIndexes.includes(index) && (
            <div className="accordion-content">{item.content}</div>
          )}
        </div>
      ))}
    </div>
  )
}