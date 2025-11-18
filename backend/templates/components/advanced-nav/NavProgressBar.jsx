import { useState } from 'react'

/**
 * NavProgressBar
 * Description: progress navigation
 */
export default function NavProgressBar({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="navprogressbar" {...props}>
      <div className="navprogressbar-content">
        {children}
      </div>
    </div>
  )
}