import { useState } from 'react'

export default function IconAccordion({ items = [] }) {
  const [openIndex, setOpenIndex] = useState(null)

  return (
    <div className="icon-accordion">
      {items.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header ${openIndex === index ? 'active' : ''}`}
            onClick={() => setOpenIndex(openIndex === index ? null : index)}
          >
            <span className="accordion-icon-left">{item.icon || '📄'}</span>
            <span>{item.title}</span>
            <span className="accordion-icon-right">{openIndex === index ? '▲' : '▼'}</span>
          </button>
          {openIndex === index && (
            <div className="accordion-content">{item.content}</div>
          )}
        </div>
      ))}
    </div>
  )
}