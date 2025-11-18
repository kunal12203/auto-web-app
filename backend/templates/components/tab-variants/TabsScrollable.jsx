import { useState } from 'react'

/**
 * TabsScrollable
 * Description: scrollable tabs
 */
export default function TabsScrollable({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tabsscrollable" {...props}>
      <div className="tabsscrollable-content">
        {children}
      </div>
    </div>
  )
}