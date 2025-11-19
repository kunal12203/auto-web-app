import { useState } from 'react'

export default function ChartRealtime({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartrealtime" {...props}>
      {children}
    </div>
  )
}