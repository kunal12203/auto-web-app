import { useState } from 'react'

export default function StepperWizard({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="stepperwizard" {...props}>
      {children}
    </div>
  )
}