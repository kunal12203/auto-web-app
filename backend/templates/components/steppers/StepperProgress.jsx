import { useState } from 'react'

export default function StepperProgress({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="stepperprogress" {...props}>
      {children}
    </div>
  )
}