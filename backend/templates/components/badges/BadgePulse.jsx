import { useState } from 'react'

export default function BadgePulse({ children, ...props }) {
  

  return (
    <div className="badgepulse" {...props}>
      {children}
    </div>
  )
}