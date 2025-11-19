import { useState } from 'react'

export default function LoaderInline({ children, ...props }) {
  

  return (
    <div className="loaderinline" {...props}>
      {children}
    </div>
  )
}