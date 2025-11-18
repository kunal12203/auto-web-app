import { useState } from 'react'

export default function DashboardAdmin({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardadmin" {...props}>
      {children}
    </div>
  )
}