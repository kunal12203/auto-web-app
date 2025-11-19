import { useState } from 'react'

export default function AvatarStatus({ children, ...props }) {
  

  return (
    <div className="avatarstatus" {...props}>
      {children}
    </div>
  )
}