import { useState } from 'react'

/**
 * LayoutMasonryGrid
 * Description: masonry grid
 */
export default function LayoutMasonryGrid({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="layoutmasonrygrid" {...props}>
      <div className="layoutmasonrygrid-content">
        {children}
      </div>
    </div>
  )
}