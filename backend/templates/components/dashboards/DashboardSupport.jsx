import { useState } from 'react'

export default function DashboardSupport({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardsupport" {...props}>
      {children}
    </div>
  )
}