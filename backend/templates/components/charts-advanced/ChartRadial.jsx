import { useState } from 'react'

export default function ChartRadial({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartradial" {...props}>
      {children}
    </div>
  )
}