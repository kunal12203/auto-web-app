import { useState } from 'react'

export default function LoaderBounce({ children, ...props }) {
  

  return (
    <div className="loaderbounce" {...props}>
      {children}
    </div>
  )
}