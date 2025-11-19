import { useState } from 'react'

export default function DashboardFinancial({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardfinancial" {...props}>
      {children}
    </div>
  )
}