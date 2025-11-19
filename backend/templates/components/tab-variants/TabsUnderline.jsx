import { useState } from 'react'

/**
 * TabsUnderline
 * Description: underline tabs
 */
export default function TabsUnderline({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tabsunderline" {...props}>
      <div className="tabsunderline-content">
        {children}
      </div>
    </div>
  )
}