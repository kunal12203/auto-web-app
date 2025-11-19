import { useState } from 'react'

export default function LoaderFullscreen({ children, ...props }) {
  

  return (
    <div className="loaderfullscreen" {...props}>
      {children}
    </div>
  )
}