import { useState } from 'react'

export default function DashboardGaming({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardgaming" {...props}>
      {children}
    </div>
  )
}