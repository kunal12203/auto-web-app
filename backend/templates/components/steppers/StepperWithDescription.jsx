import { useState } from 'react'

export default function StepperWithDescription({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="stepperwithdescription" {...props}>
      {children}
    </div>
  )
}