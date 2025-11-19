import { useState } from 'react'

export default function DashboardKPI({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardkpi" {...props}>
      {children}
    </div>
  )
}