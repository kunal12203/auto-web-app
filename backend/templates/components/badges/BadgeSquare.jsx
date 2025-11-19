import { useState } from 'react'

export default function BadgeSquare({ children, ...props }) {
  

  return (
    <div className="badgesquare" {...props}>
      {children}
    </div>
  )
}