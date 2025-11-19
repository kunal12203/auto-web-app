import { useState } from 'react'

/**
 * NavCommandPalette
 * Description: command palette
 */
export default function NavCommandPalette({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="navcommandpalette" {...props}>
      <div className="navcommandpalette-content">
        {children}
      </div>
    </div>
  )
}