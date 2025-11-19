import { useState } from 'react'

export default function AvatarFallback({ children, ...props }) {
  

  return (
    <div className="avatarfallback" {...props}>
      {children}
    </div>
  )
}