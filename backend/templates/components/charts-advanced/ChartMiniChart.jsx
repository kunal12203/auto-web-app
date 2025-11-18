import { useState } from 'react'

export default function ChartMiniChart({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartminichart" {...props}>
      {children}
    </div>
  )
}