import { useState } from 'react'

export default function LoaderIndeterminate({ children, ...props }) {
  

  return (
    <div className="loaderindeterminate" {...props}>
      {children}
    </div>
  )
}