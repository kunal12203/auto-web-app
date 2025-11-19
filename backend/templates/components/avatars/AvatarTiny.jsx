import { useState } from 'react'

export default function AvatarTiny({ children, ...props }) {
  

  return (
    <div className="avatartiny" {...props}>
      {children}
    </div>
  )
}