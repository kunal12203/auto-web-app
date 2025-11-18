import { useState } from 'react'

/**
 * ContainerCard
 * Description: card container
 */
export default function ContainerCard({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="containercard" {...props}>
      <div className="containercard-content">
        {children}
      </div>
    </div>
  )
}