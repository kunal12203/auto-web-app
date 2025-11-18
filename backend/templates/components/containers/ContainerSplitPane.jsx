import { useState } from 'react'

/**
 * ContainerSplitPane
 * Description: split pane
 */
export default function ContainerSplitPane({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="containersplitpane" {...props}>
      <div className="containersplitpane-content">
        {children}
      </div>
    </div>
  )
}