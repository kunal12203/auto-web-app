import { useState } from 'react'

export default function BadgeIcon({ children, ...props }) {
  

  return (
    <div className="badgeicon" {...props}>
      {children}
    </div>
  )
}