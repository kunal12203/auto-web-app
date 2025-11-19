import { useState } from 'react'

export default function LoaderLinear({ children, ...props }) {
  

  return (
    <div className="loaderlinear" {...props}>
      {children}
    </div>
  )
}