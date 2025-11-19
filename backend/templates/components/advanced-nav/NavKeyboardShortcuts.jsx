import { useState } from 'react'

/**
 * NavKeyboardShortcuts
 * Description: keyboard shortcuts
 */
export default function NavKeyboardShortcuts({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="navkeyboardshortcuts" {...props}>
      <div className="navkeyboardshortcuts-content">
        {children}
      </div>
    </div>
  )
}