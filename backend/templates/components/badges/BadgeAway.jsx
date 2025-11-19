import { useState } from 'react'

export default function BadgeAway({ children, ...props }) {
  

  return (
    <div className="badgeaway" {...props}>
      {children}
    </div>
  )
}