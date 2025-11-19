import { useState } from 'react'

export default function AvatarPlaceholder({ children, ...props }) {
  

  return (
    <div className="avatarplaceholder" {...props}>
      {children}
    </div>
  )
}