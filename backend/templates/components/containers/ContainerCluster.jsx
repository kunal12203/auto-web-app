import { useState } from 'react'

/**
 * ContainerCluster
 * Description: cluster container
 */
export default function ContainerCluster({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="containercluster" {...props}>
      <div className="containercluster-content">
        {children}
      </div>
    </div>
  )
}