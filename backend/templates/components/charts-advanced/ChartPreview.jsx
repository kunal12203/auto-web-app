import { useState } from 'react'

export default function ChartPreview({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartpreview" {...props}>
      {children}
    </div>
  )
}