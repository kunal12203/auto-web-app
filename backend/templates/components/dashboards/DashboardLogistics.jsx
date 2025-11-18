import { useState } from 'react'

export default function DashboardLogistics({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardlogistics" {...props}>
      {children}
    </div>
  )
}