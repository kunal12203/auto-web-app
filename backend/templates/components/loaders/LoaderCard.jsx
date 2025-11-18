import { useState } from 'react'

export default function LoaderCard({ children, ...props }) {
  

  return (
    <div className="loadercard" {...props}>
      {children}
    </div>
  )
}