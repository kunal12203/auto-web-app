import { useState } from 'react'

export default function DashboardInventory({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardinventory" {...props}>
      {children}
    </div>
  )
}