import { useState } from 'react'

export default function SearchableAccordion({ items = [] }) {
  const [searchTerm, setSearchTerm] = useState('')
  const [openIndex, setOpenIndex] = useState(null)

  const filteredItems = items.filter(item =>
    item.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
    item.content.toLowerCase().includes(searchTerm.toLowerCase())
  )

  return (
    <div className="searchable-accordion">
      <input
        type="text"
        className="accordion-search"
        placeholder="Search..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      {filteredItems.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header ${openIndex === index ? 'active' : ''}`}
            onClick={() => setOpenIndex(openIndex === index ? null : index)}
          >
            {item.title}
            <span>{openIndex === index ? '−' : '+'}</span>
          </button>
          {openIndex === index && (
            <div className="accordion-content">{item.content}</div>
          )}
        </div>
      ))}
      {filteredItems.length === 0 && <div className="no-results">No results found</div>}
    </div>
  )
}