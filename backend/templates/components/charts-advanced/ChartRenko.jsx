import { useState } from 'react'

export default function ChartRenko({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="chartrenko" {...props}>
      {children}
    </div>
  )
}