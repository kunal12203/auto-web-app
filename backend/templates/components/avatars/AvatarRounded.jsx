import { useState } from 'react'

export default function AvatarRounded({ children, ...props }) {
  

  return (
    <div className="avatarrounded" {...props}>
      {children}
    </div>
  )
}