import { useState } from 'react'

export default function AvatarEditable({ children, ...props }) {
  

  return (
    <div className="avatareditable" {...props}>
      {children}
    </div>
  )
}