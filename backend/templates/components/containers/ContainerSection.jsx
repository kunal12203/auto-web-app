import { useState } from 'react'

/**
 * ContainerSection
 * Description: section container
 */
export default function ContainerSection({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="containersection" {...props}>
      <div className="containersection-content">
        {children}
      </div>
    </div>
  )
}