import { useState } from 'react'

/**
 * TabsLazy
 * Description: lazy loaded tabs
 */
export default function TabsLazy({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tabslazy" {...props}>
      <div className="tabslazy-content">
        {children}
      </div>
    </div>
  )
}