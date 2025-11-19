import { useState } from 'react'

export default function LoaderDots({ children, ...props }) {
  

  return (
    <div className="loaderdots" {...props}>
      {children}
    </div>
  )
}