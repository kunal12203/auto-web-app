import { useState } from 'react'

export default function StepperNumber({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="steppernumber" {...props}>
      {children}
    </div>
  )
}