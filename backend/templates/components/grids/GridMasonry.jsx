import { useState } from 'react'

/**
 * GridMasonry
 * Description: masonry grid layout
 */
export default function GridMasonry({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="gridmasonry" {...props}>
      <div className="gridmasonry-content">
        {children}
      </div>
    </div>
  )
}