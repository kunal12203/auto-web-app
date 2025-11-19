import { useState } from 'react'

export default function StepperAnimated({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="stepperanimated" {...props}>
      {children}
    </div>
  )
}