import { useState } from 'react'

export default function AvatarHover({ children, ...props }) {
  

  return (
    <div className="avatarhover" {...props}>
      {children}
    </div>
  )
}