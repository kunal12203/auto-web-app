import { useState } from 'react'

export default function LoaderOverlay({ children, ...props }) {
  

  return (
    <div className="loaderoverlay" {...props}>
      {children}
    </div>
  )
}