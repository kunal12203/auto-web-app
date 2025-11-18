import { useState } from 'react'

export default function LoaderButton({ children, ...props }) {
  

  return (
    <div className="loaderbutton" {...props}>
      {children}
    </div>
  )
}