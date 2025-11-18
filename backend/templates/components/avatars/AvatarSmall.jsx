import { useState } from 'react'

export default function AvatarSmall({ children, ...props }) {
  

  return (
    <div className="avatarsmall" {...props}>
      {children}
    </div>
  )
}