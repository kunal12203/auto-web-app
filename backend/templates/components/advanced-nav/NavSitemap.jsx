import { useState } from 'react'

/**
 * NavSitemap
 * Description: sitemap navigation
 */
export default function NavSitemap({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="navsitemap" {...props}>
      <div className="navsitemap-content">
        {children}
      </div>
    </div>
  )
}