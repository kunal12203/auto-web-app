import { useEffect, useState } from 'react'

export default function ControlledAccordion({ items = [], activeIndex = null, onChange }) {
  const [internalIndex, setInternalIndex] = useState(activeIndex)

  useEffect(() => {
    setInternalIndex(activeIndex)
  }, [activeIndex])

  const handleToggle = (index) => {
    const newIndex = internalIndex === index ? null : index
    setInternalIndex(newIndex)
    if (onChange) onChange(newIndex)
  }

  return (
    <div className="controlled-accordion">
      {items.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header ${internalIndex === index ? 'active' : ''}`}
            onClick={() => handleToggle(index)}
          >
            {item.title}
            <span>{internalIndex === index ? '−' : '+'}</span>
          </button>
          {internalIndex === index && (
            <div className="accordion-content">{item.content}</div>
          )}
        </div>
      ))}
    </div>
  )
}