import { useState } from 'react'

export default function LoaderPulse({ children, ...props }) {
  

  return (
    <div className="loaderpulse" {...props}>
      {children}
    </div>
  )
}