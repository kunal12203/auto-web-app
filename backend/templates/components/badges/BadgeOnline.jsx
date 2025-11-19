import { useState } from 'react'

export default function BadgeOnline({ children, ...props }) {
  

  return (
    <div className="badgeonline" {...props}>
      {children}
    </div>
  )
}