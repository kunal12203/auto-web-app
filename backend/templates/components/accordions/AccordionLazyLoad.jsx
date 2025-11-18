import { useState } from 'react'

export default function LazyAccordion({ items = [], onLoadContent }) {
  const [openIndex, setOpenIndex] = useState(null)
  const [loadedContent, setLoadedContent] = useState({})

  const handleToggle = async (index) => {
    if (openIndex === index) {
      setOpenIndex(null)
      return
    }

    setOpenIndex(index)

    if (!loadedContent[index] && onLoadContent) {
      const content = await onLoadContent(items[index])
      setLoadedContent(prev => ({ ...prev, [index]: content }))
    }
  }

  return (
    <div className="lazy-accordion">
      {items.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header ${openIndex === index ? 'active' : ''}`}
            onClick={() => handleToggle(index)}
          >
            {item.title}
            <span>{openIndex === index ? '−' : '+'}</span>
          </button>
          {openIndex === index && (
            <div className="accordion-content">
              {loadedContent[index] || item.content || 'Loading...'}
            </div>
          )}
        </div>
      ))}
    </div>
  )
}