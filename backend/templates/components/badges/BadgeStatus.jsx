import { useState } from 'react'

export default function BadgeStatus({ children, ...props }) {
  

  return (
    <div className="badgestatus" {...props}>
      {children}
    </div>
  )
}