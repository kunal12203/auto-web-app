import { useState } from 'react'

export default function StepperValidated({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="steppervalidated" {...props}>
      {children}
    </div>
  )
}