import { useState } from 'react'

export default function ChartCombo({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartcombo" {...props}>
      {children}
    </div>
  )
}