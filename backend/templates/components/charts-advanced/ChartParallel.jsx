import { useState } from 'react'

export default function ChartParallel({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartparallel" {...props}>
      {children}
    </div>
  )
}