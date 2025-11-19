import { useState } from 'react'

export default function AvatarInitials({ children, ...props }) {
  

  return (
    <div className="avatarinitials" {...props}>
      {children}
    </div>
  )
}