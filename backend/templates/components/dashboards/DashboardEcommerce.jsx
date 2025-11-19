import { useState } from 'react'

export default function DashboardEcommerce({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardecommerce" {...props}>
      {children}
    </div>
  )
}