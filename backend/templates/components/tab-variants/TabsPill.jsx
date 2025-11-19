import { useState } from 'react'

/**
 * TabsPill
 * Description: pill-style tabs
 */
export default function TabsPill({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tabspill" {...props}>
      <div className="tabspill-content">
        {children}
      </div>
    </div>
  )
}