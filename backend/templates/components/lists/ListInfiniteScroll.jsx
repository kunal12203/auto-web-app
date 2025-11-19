import { useState } from 'react'

/**
 * ListInfiniteScroll
 * Description: infinite scrolling list
 */
export default function ListInfiniteScroll({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="listinfinitescroll" {...props}>
      <div className="listinfinitescroll-content">
        {children}
      </div>
    </div>
  )
}