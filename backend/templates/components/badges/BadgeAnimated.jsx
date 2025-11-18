import { useState } from 'react'

export default function BadgeAnimated({ children, ...props }) {
  

  return (
    <div className="badgeanimated" {...props}>
      {children}
    </div>
  )
}