import { useState } from 'react'

export default function StepperCollapsible({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="steppercollapsible" {...props}>
      {children}
    </div>
  )
}