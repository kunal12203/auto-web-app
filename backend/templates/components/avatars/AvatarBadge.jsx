import { useState } from 'react'

export default function AvatarBadge({ children, ...props }) {
  

  return (
    <div className="avatarbadge" {...props}>
      {children}
    </div>
  )
}