import { useState } from 'react'

export default function Accordion({ items = [] }) {
  const [openIndex, setOpenIndex] = useState(null)

  const defaultItems = [
    { title: '{{ACCORDION_ITEM_1_TITLE}}', content: '{{ACCORDION_ITEM_1_CONTENT}}' },
    { title: '{{ACCORDION_ITEM_2_TITLE}}', content: '{{ACCORDION_ITEM_2_CONTENT}}' },
    { title: '{{ACCORDION_ITEM_3_TITLE}}', content: '{{ACCORDION_ITEM_3_CONTENT}}' }
  ]

  const accordionItems = items.length > 0 ? items : defaultItems

  return (
    <div className="accordion">
      {accordionItems.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header ${openIndex === index ? 'active' : ''}`}
            onClick={() => setOpenIndex(openIndex === index ? null : index)}
          >
            <span>{item.title}</span>
            <span className="accordion-icon">{openIndex === index ? '−' : '+'}</span>
          </button>
          {openIndex === index && (
            <div className="accordion-content">{item.content}</div>
          )}
        </div>
      ))}
    </div>
  )
}