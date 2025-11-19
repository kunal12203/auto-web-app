import { useState } from 'react'

export default function AvatarStack({ children, ...props }) {
  

  return (
    <div className="avatarstack" {...props}>
      {children}
    </div>
  )
}