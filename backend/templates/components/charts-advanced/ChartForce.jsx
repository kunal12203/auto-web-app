import { useState } from 'react'

export default function ChartForce({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartforce" {...props}>
      {children}
    </div>
  )
}