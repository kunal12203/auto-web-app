import { useState } from 'react'

export default function ChartFunnel({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartfunnel" {...props}>
      {children}
    </div>
  )
}