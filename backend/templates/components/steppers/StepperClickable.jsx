import { useState } from 'react'

export default function StepperClickable({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="stepperclickable" {...props}>
      {children}
    </div>
  )
}