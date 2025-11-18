import { useState } from 'react'

export default function ChartViolin({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartviolin" {...props}>
      {children}
    </div>
  )
}