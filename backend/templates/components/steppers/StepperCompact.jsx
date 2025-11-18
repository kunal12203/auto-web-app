import { useState } from 'react'

export default function StepperCompact({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="steppercompact" {...props}>
      {children}
    </div>
  )
}