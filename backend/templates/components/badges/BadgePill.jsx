import { useState } from 'react'

export default function BadgePill({ children, ...props }) {
  

  return (
    <div className="badgepill" {...props}>
      {children}
    </div>
  )
}