import { useState } from 'react'

export default function AvatarClickable({ children, ...props }) {
  

  return (
    <div className="avatarclickable" {...props}>
      {children}
    </div>
  )
}