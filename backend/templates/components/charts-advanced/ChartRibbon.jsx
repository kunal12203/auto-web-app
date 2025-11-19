import { useState } from 'react'

export default function ChartRibbon({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartribbon" {...props}>
      {children}
    </div>
  )
}