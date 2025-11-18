import { useState } from 'react'

/**
 * ContainerResizablePanes
 * Description: resizable panes
 */
export default function ContainerResizablePanes({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="containerresizablepanes" {...props}>
      <div className="containerresizablepanes-content">
        {children}
      </div>
    </div>
  )
}