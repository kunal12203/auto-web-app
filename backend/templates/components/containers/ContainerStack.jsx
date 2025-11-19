import { useState } from 'react'

/**
 * ContainerStack
 * Description: stack container
 */
export default function ContainerStack({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="containerstack" {...props}>
      <div className="containerstack-content">
        {children}
      </div>
    </div>
  )
}