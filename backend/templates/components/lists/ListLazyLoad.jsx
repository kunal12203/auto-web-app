import { useState } from 'react'

/**
 * ListLazyLoad
 * Description: lazy loading list
 */
export default function ListLazyLoad({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="listlazyload" {...props}>
      <div className="listlazyload-content">
        {children}
      </div>
    </div>
  )
}