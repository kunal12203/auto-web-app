import { useState } from 'react'

export default function LoaderPage({ children, ...props }) {
  

  return (
    <div className="loaderpage" {...props}>
      {children}
    </div>
  )
}