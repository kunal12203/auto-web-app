import { useState } from 'react'

/**
 * ListVirtual
 * Description: virtualized list for performance
 */
export default function ListVirtual({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="listvirtual" {...props}>
      <div className="listvirtual-content">
        {children}
      </div>
    </div>
  )
}