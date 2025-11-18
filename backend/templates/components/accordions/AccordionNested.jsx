import { useState } from 'react'

export default function NestedAccordion({ items = [] }) {
  const [openIndexes, setOpenIndexes] = useState({})

  const toggleItem = (path) => {
    setOpenIndexes(prev => ({ ...prev, [path]: !prev[path] }))
  }

  const renderItems = (items, parentPath = '') => {
    return items.map((item, index) => {
      const currentPath = parentPath ? `${parentPath}.${index}` : `${index}`
      const isOpen = openIndexes[currentPath]

      return (
        <div key={currentPath} className="nested-accordion-item" style={{ marginLeft: parentPath ? '20px' : '0' }}>
          <button
            className={`accordion-header ${isOpen ? 'active' : ''}`}
            onClick={() => toggleItem(currentPath)}
          >
            {item.title}
            <span>{isOpen ? '−' : '+'}</span>
          </button>
          {isOpen && item.content && <div className="accordion-content">{item.content}</div>}
          {isOpen && item.children && renderItems(item.children, currentPath)}
        </div>
      )
    })
  }

  return <div className="nested-accordion">{renderItems(items)}</div>
}