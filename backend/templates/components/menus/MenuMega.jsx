import { useState } from 'react'

export default function MegaMenu({ sections = [] }) {
  const [activeSection, setActiveSection] = useState(null)

  return (
    <div className="mega-menu">
      <div className="mega-menu-trigger">
        {sections.map((section, index) => (
          <button
            key={index}
            className={`menu-section-trigger ${activeSection === index ? 'active' : ''}`}
            onMouseEnter={() => setActiveSection(index)}
          >
            {section.label}
          </button>
        ))}
      </div>

      {activeSection !== null && (
        <div className="mega-menu-content" onMouseLeave={() => setActiveSection(null)}>
          <div className="mega-menu-grid">
            {sections[activeSection].columns.map((column, colIndex) => (
              <div key={colIndex} className="mega-menu-column">
                <h3>{column.title}</h3>
                {column.items.map((item, itemIndex) => (
                  <a key={itemIndex} href={item.href} className="mega-menu-item">
                    {item.label}
                  </a>
                ))}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}