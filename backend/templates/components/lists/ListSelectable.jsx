import { useState } from 'react'

/**
 * ListSelectable
 * Description: list with multi-select
 */
export default function ListSelectable({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="listselectable" {...props}>
      <div className="listselectable-content">
        {children}
      </div>
    </div>
  )
}