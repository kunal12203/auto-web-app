import { useState } from 'react'

export default function LoaderCustom({ children, ...props }) {
  

  return (
    <div className="loadercustom" {...props}>
      {children}
    </div>
  )
}