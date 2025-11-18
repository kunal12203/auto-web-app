import { useState } from 'react'

/**
 * TabsIcon
 * Description: icon tabs
 */
export default function TabsIcon({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tabsicon" {...props}>
      <div className="tabsicon-content">
        {children}
      </div>
    </div>
  )
}