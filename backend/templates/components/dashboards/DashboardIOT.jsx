import { useState } from 'react'

export default function DashboardIOT({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardiot" {...props}>
      {children}
    </div>
  )
}