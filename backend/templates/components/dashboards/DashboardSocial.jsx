import { useState } from 'react'

export default function DashboardSocial({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardsocial" {...props}>
      {children}
    </div>
  )
}