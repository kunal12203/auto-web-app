import { useState } from 'react'

/**
 * ProductRecentlyViewed
 * Description: recently viewed products
 */
export default function ProductRecentlyViewed({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="productrecentlyviewed" {...props}>
      <div className="productrecentlyviewed-content">
        {children}
      </div>
    </div>
  )
}