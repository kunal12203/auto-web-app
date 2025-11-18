import { useState } from 'react'

export default function StepperWithProgress({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="stepperwithprogress" {...props}>
      {children}
    </div>
  )
}