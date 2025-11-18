import { useState } from 'react'

export default function ChartWordCloud({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartwordcloud" {...props}>
      {children}
    </div>
  )
}