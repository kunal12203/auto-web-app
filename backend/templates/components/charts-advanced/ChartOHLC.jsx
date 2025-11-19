import { useState } from 'react'

export default function ChartOHLC({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartohlc" {...props}>
      {children}
    </div>
  )
}