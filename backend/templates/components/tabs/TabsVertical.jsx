import { useState } from 'react'

export default function TabsVertical() {
  const [activeTab, setActiveTab] = useState(0)

  const tabs = [
    { title: 'Tab 1', content: 'Content 1' },
    { title: 'Tab 2', content: 'Content 2' },
    { title: 'Tab 3', content: 'Content 3' }
  ]

  return (
    <section className="tabs-vertical">
      <div className="container">
        <div className="tabs-vertical-container">
          <div className="tab-sidebar">
            {tabs.map((tab, i) => (
              <button
                key={i}
                className={activeTab === i ? 'active' : ''}
                onClick={() => setActiveTab(i)}
              >
                {tab.title}
              </button>
            ))}
          </div>
          <div className="tab-content-area">
            <p>{tabs[activeTab].content}</p>
          </div>
        </div>
      </div>
    </section>
  )
}