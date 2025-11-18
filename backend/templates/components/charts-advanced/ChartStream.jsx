import { useState } from 'react'

export default function ChartStream({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartstream" {...props}>
      {children}
    </div>
  )
}