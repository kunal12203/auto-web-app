import { useState } from 'react'

export default function LoaderRing({ children, ...props }) {
  

  return (
    <div className="loaderring" {...props}>
      {children}
    </div>
  )
}