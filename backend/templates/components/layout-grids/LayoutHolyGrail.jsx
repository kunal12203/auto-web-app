import { useState } from 'react'

/**
 * LayoutHolyGrail
 * Description: holy grail layout
 */
export default function LayoutHolyGrail({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="layoutholygrail" {...props}>
      <div className="layoutholygrail-content">
        {children}
      </div>
    </div>
  )
}