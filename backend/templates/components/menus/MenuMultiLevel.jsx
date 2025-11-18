import { useState } from 'react'

export default function MultiLevelMenu({ items = [] }) {
  const [expandedItems, setExpandedItems] = useState({})

  const toggleItem = (path) => {
    setExpandedItems(prev => ({ ...prev, [path]: !prev[path] }))
  }

  const renderItems = (items, level = 0, parentPath = '') => {
    return items.map((item, index) => {
      const currentPath = parentPath ? `${parentPath}.${index}` : `${index}`
      const hasChildren = item.children && item.children.length > 0
      const isExpanded = expandedItems[currentPath]

      return (
        <div key={currentPath} style={{ marginLeft: level * 20 }}>
          <button
            className={`menu-item level-${level} ${hasChildren ? 'has-children' : ''}`}
            onClick={() => hasChildren ? toggleItem(currentPath) : item.onClick?.()}
          >
            {item.icon && <span className="menu-icon">{item.icon}</span>}
            <span>{item.label}</span>
            {hasChildren && <span>{isExpanded ? '▼' : '▶'}</span>}
          </button>
          {hasChildren && isExpanded && renderItems(item.children, level + 1, currentPath)}
        </div>
      )
    })
  }

  return <div className="multi-level-menu">{renderItems(items)}</div>
}