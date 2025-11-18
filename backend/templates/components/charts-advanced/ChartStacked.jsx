import { useState } from 'react'

export default function ChartStacked({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartstacked" {...props}>
      {children}
    </div>
  )
}