import { useState } from 'react'

export default function ChartKagi({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartkagi" {...props}>
      {children}
    </div>
  )
}