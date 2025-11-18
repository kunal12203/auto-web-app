import { useState } from 'react'

export default function ChartHistogram({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="charthistogram" {...props}>
      {children}
    </div>
  )
}