import { useState } from 'react'

export default function DashboardMetrics({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardmetrics" {...props}>
      {children}
    </div>
  )
}