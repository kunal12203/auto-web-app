import { useState } from 'react'

export default function BadgeOutlined({ children, ...props }) {
  

  return (
    <div className="badgeoutlined" {...props}>
      {children}
    </div>
  )
}