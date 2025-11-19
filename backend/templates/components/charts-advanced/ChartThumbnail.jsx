import { useState } from 'react'

export default function ChartThumbnail({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartthumbnail" {...props}>
      {children}
    </div>
  )
}