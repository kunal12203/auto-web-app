import { useState } from 'react'

export default function AvatarWithTooltip({ children, ...props }) {
  

  return (
    <div className="avatarwithtooltip" {...props}>
      {children}
    </div>
  )
}