import { useState } from 'react'

export default function StepperDots({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="stepperdots" {...props}>
      {children}
    </div>
  )
}