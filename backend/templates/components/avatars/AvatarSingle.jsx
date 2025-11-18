import { useState } from 'react'

export default function AvatarSingle({ children, ...props }) {
  

  return (
    <div className="avatarsingle" {...props}>
      {children}
    </div>
  )
}