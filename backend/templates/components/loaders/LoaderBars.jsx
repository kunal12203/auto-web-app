import { useState } from 'react'

export default function LoaderBars({ children, ...props }) {
  

  return (
    <div className="loaderbars" {...props}>
      {children}
    </div>
  )
}