import { useState } from 'react'

/**
 * ImageAvatarGroup
 * Description: avatar group
 */
export default function ImageAvatarGroup({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="imageavatargroup" {...props}>
      <div className="imageavatargroup-content">
        {children}
      </div>
    </div>
  )
}