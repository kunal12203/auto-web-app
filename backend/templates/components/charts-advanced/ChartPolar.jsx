import { useState } from 'react'

export default function ChartPolar({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartpolar" {...props}>
      {children}
    </div>
  )
}