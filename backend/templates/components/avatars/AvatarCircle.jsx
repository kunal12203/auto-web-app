import { useState } from 'react'

export default function AvatarCircle({ children, ...props }) {
  

  return (
    <div className="avatarcircle" {...props}>
      {children}
    </div>
  )
}