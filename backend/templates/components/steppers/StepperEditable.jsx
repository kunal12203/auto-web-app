import { useState } from 'react'

export default function StepperEditable({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="steppereditable" {...props}>
      {children}
    </div>
  )
}