import { useState } from 'react'

export default function ChartZoomable({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartzoomable" {...props}>
      {children}
    </div>
  )
}