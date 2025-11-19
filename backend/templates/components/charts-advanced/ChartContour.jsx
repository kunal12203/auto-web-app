import { useState } from 'react'

export default function ChartContour({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartcontour" {...props}>
      {children}
    </div>
  )
}