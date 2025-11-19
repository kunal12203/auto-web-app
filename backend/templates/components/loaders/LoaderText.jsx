import { useState } from 'react'

export default function LoaderText({ children, ...props }) {
  

  return (
    <div className="loadertext" {...props}>
      {children}
    </div>
  )
}