import { useState } from 'react'

export default function MiniDrawer({ children }) {
  const [isExpanded, setIsExpanded] = useState(false)

  return (
    <div className={`drawer drawer-mini ${isExpanded ? 'expanded' : 'mini'}`}>
      <button className="drawer-toggle" onClick={() => setIsExpanded(!isExpanded)}>
        {isExpanded ? '◀' : '▶'}
      </button>
      <div className="drawer-content">{children}</div>
    </div>
  )
}