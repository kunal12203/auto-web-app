import { useState } from 'react'

export default function LoaderDeterminate({ children, ...props }) {
  

  return (
    <div className="loaderdeterminate" {...props}>
      {children}
    </div>
  )
}