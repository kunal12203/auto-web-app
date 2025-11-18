import { useState } from 'react'

export default function DashboardEducation({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="dashboardeducation" {...props}>
      {children}
    </div>
  )
}