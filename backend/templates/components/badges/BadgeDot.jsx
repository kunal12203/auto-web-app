import { useState } from 'react'

export default function BadgeDot({ children, ...props }) {
  

  return (
    <div className="badgedot" {...props}>
      {children}
    </div>
  )
}