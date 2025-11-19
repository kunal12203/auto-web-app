import { useState } from 'react'

export default function TabsSimple() {
  const [activeTab, setActiveTab] = useState(0)
  
  const tabs = [
    { title: '{{TAB_1_TITLE}}', content: '{{TAB_1_CONTENT}}' },
    { title: '{{TAB_2_TITLE}}', content: '{{TAB_2_CONTENT}}' },
    { title: '{{TAB_3_TITLE}}', content: '{{TAB_3_CONTENT}}' }
  ]

  return (
    <section className="tabs-simple">
      <div className="container">
        <div className="tab-buttons">
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
        <div className="tab-content">
          <p>{tabs[activeTab].content}</p>
        </div>
      </div>
    </section>
  )
}