import { useState } from 'react'

export default function DashboardCRM({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardcrm" {...props}>
      {children}
    </div>
  )
}