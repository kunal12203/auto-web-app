import { useState } from 'react'

export default function StepperConnector({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="stepperconnector" {...props}>
      {children}
    </div>
  )
}