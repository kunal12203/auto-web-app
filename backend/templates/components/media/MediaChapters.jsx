import { useState } from 'react'

/**
 * MediaChapters
 * Description: video chapters
 */
export default function MediaChapters({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="mediachapters" {...props}>
      <div className="mediachapters-content">
        {children}
      </div>
    </div>
  )
}