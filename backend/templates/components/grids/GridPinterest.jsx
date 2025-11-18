import { useState } from 'react'

/**
 * GridPinterest
 * Description: Pinterest-style grid
 */
export default function GridPinterest({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="gridpinterest" {...props}>
      <div className="gridpinterest-content">
        {children}
      </div>
    </div>
  )
}