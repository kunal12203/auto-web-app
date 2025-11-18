import { useState } from 'react'

export default function ChartChord({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartchord" {...props}>
      {children}
    </div>
  )
}