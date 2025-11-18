import { useState } from 'react'

export default function BadgeRemovable({ children, ...props }) {
  

  return (
    <div className="badgeremovable" {...props}>
      {children}
    </div>
  )
}