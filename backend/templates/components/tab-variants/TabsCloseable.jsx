import { useState } from 'react'

/**
 * TabsCloseable
 * Description: closeable tabs
 */
export default function TabsCloseable({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tabscloseable" {...props}>
      <div className="tabscloseable-content">
        {children}
      </div>
    </div>
  )
}