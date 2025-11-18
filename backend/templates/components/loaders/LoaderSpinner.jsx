import { useState } from 'react'

export default function LoaderSpinner({ children, ...props }) {
  

  return (
    <div className="loaderspinner" {...props}>
      {children}
    </div>
  )
}