import { useState } from 'react'

export default function StepperVertical({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="steppervertical" {...props}>
      {children}
    </div>
  )
}