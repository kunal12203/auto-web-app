import { useState } from 'react'

export default function DashboardRealEstate({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardrealestate" {...props}>
      {children}
    </div>
  )
}