import { useState } from 'react'

export default function DashboardAnalytics({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardanalytics" {...props}>
      {children}
    </div>
  )
}