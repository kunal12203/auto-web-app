import { useState } from 'react'

export default function DashboardMarketing({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardmarketing" {...props}>
      {children}
    </div>
  )
}