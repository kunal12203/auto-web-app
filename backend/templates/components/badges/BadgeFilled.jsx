import { useState } from 'react'

export default function BadgeFilled({ children, ...props }) {
  

  return (
    <div className="badgefilled" {...props}>
      {children}
    </div>
  )
}