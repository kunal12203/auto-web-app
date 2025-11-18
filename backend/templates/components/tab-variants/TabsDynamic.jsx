import { useState } from 'react'

/**
 * TabsDynamic
 * Description: dynamic tabs
 */
export default function TabsDynamic({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tabsdynamic" {...props}>
      <div className="tabsdynamic-content">
        {children}
      </div>
    </div>
  )
}