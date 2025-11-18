import { useState } from 'react'

/**
 * GridFilterable
 * Description: filterable grid
 */
export default function GridFilterable({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="gridfilterable" {...props}>
      <div className="gridfilterable-content">
        {children}
      </div>
    </div>
  )
}