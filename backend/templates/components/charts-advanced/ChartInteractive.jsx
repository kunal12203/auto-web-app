import { useState } from 'react'

export default function ChartInteractive({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartinteractive" {...props}>
      {children}
    </div>
  )
}