import { useState } from 'react'

export default function AvatarLarge({ children, ...props }) {
  

  return (
    <div className="avatarlarge" {...props}>
      {children}
    </div>
  )
}