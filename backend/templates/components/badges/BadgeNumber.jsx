import { useState } from 'react'

export default function BadgeNumber({ children, ...props }) {
  

  return (
    <div className="badgenumber" {...props}>
      {children}
    </div>
  )
}