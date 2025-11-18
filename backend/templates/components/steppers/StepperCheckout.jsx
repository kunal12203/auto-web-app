import { useState } from 'react'

export default function StepperCheckout({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="steppercheckout" {...props}>
      {children}
    </div>
  )
}