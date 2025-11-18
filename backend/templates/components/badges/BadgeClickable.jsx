import { useState } from 'react'

export default function BadgeClickable({ children, ...props }) {
  

  return (
    <div className="badgeclickable" {...props}>
      {children}
    </div>
  )
}