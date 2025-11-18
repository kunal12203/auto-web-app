import { useState } from 'react'

export default function BadgeOffline({ children, ...props }) {
  

  return (
    <div className="badgeoffline" {...props}>
      {children}
    </div>
  )
}