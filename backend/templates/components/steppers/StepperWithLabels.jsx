import { useState } from 'react'

export default function StepperWithLabels({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="stepperwithlabels" {...props}>
      {children}
    </div>
  )
}