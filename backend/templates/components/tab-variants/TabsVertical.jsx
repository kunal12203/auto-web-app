import { useState } from 'react'

/**
 * TabsVertical
 * Description: vertical tabs
 */
export default function TabsVertical({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tabsvertical" {...props}>
      <div className="tabsvertical-content">
        {children}
      </div>
    </div>
  )
}