import { useState } from 'react'

export default function StepperHorizontal({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="stepperhorizontal" {...props}>
      {children}
    </div>
  )
}