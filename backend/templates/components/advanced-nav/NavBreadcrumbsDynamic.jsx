import { useState } from 'react'

/**
 * NavBreadcrumbsDynamic
 * Description: dynamic breadcrumbs
 */
export default function NavBreadcrumbsDynamic({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="navbreadcrumbsdynamic" {...props}>
      <div className="navbreadcrumbsdynamic-content">
        {children}
      </div>
    </div>
  )
}