import { useState } from 'react'

export default function StepperResponsive({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="stepperresponsive" {...props}>
      {children}
    </div>
  )
}