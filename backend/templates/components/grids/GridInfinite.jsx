import { useState } from 'react'

/**
 * GridInfinite
 * Description: infinite scroll grid
 */
export default function GridInfinite({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="gridinfinite" {...props}>
      <div className="gridinfinite-content">
        {children}
      </div>
    </div>
  )
}