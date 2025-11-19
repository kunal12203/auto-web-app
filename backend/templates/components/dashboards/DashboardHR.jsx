import { useState } from 'react'

export default function DashboardHR({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardhr" {...props}>
      {children}
    </div>
  )
}