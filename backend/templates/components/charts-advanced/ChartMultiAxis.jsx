import { useState } from 'react'

export default function ChartMultiAxis({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartmultiaxis" {...props}>
      {children}
    </div>
  )
}