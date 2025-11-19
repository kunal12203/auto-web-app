import { useState } from 'react'

export default function StepperDesktop({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="stepperdesktop" {...props}>
      {children}
    </div>
  )
}