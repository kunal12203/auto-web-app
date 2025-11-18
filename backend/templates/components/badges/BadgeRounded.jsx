import { useState } from 'react'

export default function BadgeRounded({ children, ...props }) {
  

  return (
    <div className="badgerounded" {...props}>
      {children}
    </div>
  )
}