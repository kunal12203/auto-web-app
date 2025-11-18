import { useState } from 'react'

export default function ChartBullet({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartbullet" {...props}>
      {children}
    </div>
  )
}