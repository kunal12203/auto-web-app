import { useState } from 'react'

export default function DashboardSales({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardsales" {...props}>
      {children}
    </div>
  )
}