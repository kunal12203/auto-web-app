import { useState } from 'react'

export default function StepperLinear({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="stepperlinear" {...props}>
      {children}
    </div>
  )
}