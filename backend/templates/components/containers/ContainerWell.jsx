import { useState } from 'react'

/**
 * ContainerWell
 * Description: well container
 */
export default function ContainerWell({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="containerwell" {...props}>
      <div className="containerwell-content">
        {children}
      </div>
    </div>
  )
}