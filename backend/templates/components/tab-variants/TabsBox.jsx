import { useState } from 'react'

/**
 * TabsBox
 * Description: box tabs
 */
export default function TabsBox({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tabsbox" {...props}>
      <div className="tabsbox-content">
        {children}
      </div>
    </div>
  )
}