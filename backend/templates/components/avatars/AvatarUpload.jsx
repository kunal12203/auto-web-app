import { useState } from 'react'

export default function AvatarUpload({ children, ...props }) {
  

  return (
    <div className="avatarupload" {...props}>
      {children}
    </div>
  )
}