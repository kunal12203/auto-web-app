import { useState } from 'react'

/**
 * ProductWishlistBtn
 * Description: wishlist button
 */
export default function ProductWishlistBtn({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="productwishlistbtn" {...props}>
      <div className="productwishlistbtn-content">
        {children}
      </div>
    </div>
  )
}