import { useState } from 'react'

export default function AvatarSquare({ children, ...props }) {
  

  return (
    <div className="avatarsquare" {...props}>
      {children}
    </div>
  )
}