import { useState } from 'react'

export default function LoaderCircle({ children, ...props }) {
  

  return (
    <div className="loadercircle" {...props}>
      {children}
    </div>
  )
}