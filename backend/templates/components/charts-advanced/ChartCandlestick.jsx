import { useState } from 'react'

export default function ChartCandlestick({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartcandlestick" {...props}>
      {children}
    </div>
  )
}