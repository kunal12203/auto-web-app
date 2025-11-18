import { useState } from 'react'

export default function BadgeCounter({ children, ...props }) {
  

  return (
    <div className="badgecounter" {...props}>
      {children}
    </div>
  )
}