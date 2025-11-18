import { useState } from 'react'

export default function ChartWaterfall({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartwaterfall" {...props}>
      {children}
    </div>
  )
}