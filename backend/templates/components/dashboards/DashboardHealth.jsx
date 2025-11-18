import { useState } from 'react'

export default function DashboardHealth({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardhealth" {...props}>
      {children}
    </div>
  )
}