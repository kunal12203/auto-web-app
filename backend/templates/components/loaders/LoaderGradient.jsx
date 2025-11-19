import { useState } from 'react'

export default function LoaderGradient({ children, ...props }) {
  

  return (
    <div className="loadergradient" {...props}>
      {children}
    </div>
  )
}