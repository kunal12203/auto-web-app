import { useState } from 'react'

export default function AnimatedAccordion({ items = [] }) {
  const [openIndex, setOpenIndex] = useState(null)

  return (
    <div className="animated-accordion">
      {items.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header ${openIndex === index ? 'active' : ''}`}
            onClick={() => setOpenIndex(openIndex === index ? null : index)}
          >
            <span>{item.title}</span>
            <span className="icon-rotate">{openIndex === index ? '−' : '+'}</span>
          </button>
          <div className={`accordion-content-wrapper ${openIndex === index ? 'open' : 'closed'}`}>
            <div className="accordion-content">{item.content}</div>
          </div>
        </div>
      ))}
    </div>
  )
}