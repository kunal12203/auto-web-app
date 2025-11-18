import { useState } from 'react'

export default function BadgeGradient({ children, ...props }) {
  

  return (
    <div className="badgegradient" {...props}>
      {children}
    </div>
  )
}