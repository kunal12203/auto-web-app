import { useState } from 'react'

export default function BadgeNotification({ children, ...props }) {
  

  return (
    <div className="badgenotification" {...props}>
      {children}
    </div>
  )
}