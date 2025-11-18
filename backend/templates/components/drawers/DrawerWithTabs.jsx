import { useState } from 'react'

export default function TabDrawer({ isOpen, onClose, tabs = [] }) {
  const [activeTab, setActiveTab] = useState(0)

  return (
    <>
      {isOpen && <div className="drawer-overlay" onClick={onClose} />}
      <div className={`drawer drawer-with-tabs ${isOpen ? 'open' : ''}`}>
        <button className="drawer-close" onClick={onClose}>×</button>
        <div className="drawer-tabs">
          {tabs.map((tab, index) => (
            <button
              key={index}
              className={`tab ${activeTab === index ? 'active' : ''}`}
              onClick={() => setActiveTab(index)}
            >
              {tab.label}
            </button>
          ))}
        </div>
        <div className="drawer-content">
          {tabs[activeTab]?.content}
        </div>
      </div>
    </>
  )
}