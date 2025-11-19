import { useState } from 'react'

export default function AvatarBordered({ children, ...props }) {
  

  return (
    <div className="avatarbordered" {...props}>
      {children}
    </div>
  )
}