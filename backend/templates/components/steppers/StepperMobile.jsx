import { useState } from 'react'

export default function StepperMobile({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="steppermobile" {...props}>
      {children}
    </div>
  )
}