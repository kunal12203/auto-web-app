import { useState } from 'react'

export default function LoaderCircular({ children, ...props }) {
  

  return (
    <div className="loadercircular" {...props}>
      {children}
    </div>
  )
}