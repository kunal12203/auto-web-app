import { useState } from 'react'

/**
 * ContainerJumbotron
 * Description: jumbotron
 */
export default function ContainerJumbotron({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="containerjumbotron" {...props}>
      <div className="containerjumbotron-content">
        {children}
      </div>
    </div>
  )
}