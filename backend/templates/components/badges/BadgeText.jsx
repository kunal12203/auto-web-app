import { useState } from 'react'

export default function BadgeText({ children, ...props }) {
  

  return (
    <div className="badgetext" {...props}>
      {children}
    </div>
  )
}