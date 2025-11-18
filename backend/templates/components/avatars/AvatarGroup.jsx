import { useState } from 'react'

export default function AvatarGroup({ children, ...props }) {
  

  return (
    <div className="avatargroup" {...props}>
      {children}
    </div>
  )
}