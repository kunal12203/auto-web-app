import { useState } from 'react'

export default function DashboardProject({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardproject" {...props}>
      {children}
    </div>
  )
}