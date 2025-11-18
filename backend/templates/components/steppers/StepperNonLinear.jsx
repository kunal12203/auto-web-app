import { useState } from 'react'

export default function StepperNonLinear({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="steppernonlinear" {...props}>
      {children}
    </div>
  )
}