import { useState } from 'react'

/**
 * TabsNested
 * Description: nested tabs
 */
export default function TabsNested({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tabsnested" {...props}>
      <div className="tabsnested-content">
        {children}
      </div>
    </div>
  )
}