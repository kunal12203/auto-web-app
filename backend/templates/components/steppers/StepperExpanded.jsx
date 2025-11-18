import { useState } from 'react'

export default function StepperExpanded({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="stepperexpanded" {...props}>
      {children}
    </div>
  )
}