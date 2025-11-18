import { useState } from 'react'

export default function AccordionMultiple() {
  const [openItems, setOpenItems] = useState([])

  const items = [
    { title: '{{ACCORDION_1_TITLE}}', content: '{{ACCORDION_1_CONTENT}}' },
    { title: '{{ACCORDION_2_TITLE}}', content: '{{ACCORDION_2_CONTENT}}' },
    { title: '{{ACCORDION_3_TITLE}}', content: '{{ACCORDION_3_CONTENT}}' }
  ]

  const toggleItem = (index) => {
    setOpenItems(prev =>
      prev.includes(index)
        ? prev.filter(i => i !== index)
        : [...prev, index]
    )
  }

  return (
    <section className="accordion-multiple">
      <div className="container">
        {items.map((item, i) => (
          <div key={i} className="accordion-item">
            <button
              className="accordion-header"
              onClick={() => toggleItem(i)}
            >
              {item.title}
            </button>
            {openItems.includes(i) && (
              <div className="accordion-content">{item.content}</div>
            )}
          </div>
        ))}
      </div>
    </section>
  )
}