import { useState } from 'react'

export default function StepperIcon({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="steppericon" {...props}>
      {children}
    </div>
  )
}