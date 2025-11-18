import { useState } from 'react'

/**
 * CheckoutCartSummary
 * Description: cart summary
 */
export default function CheckoutCartSummary({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="checkoutcartsummary" {...props}>
      <div className="checkoutcartsummary-content">
        {children}
      </div>
    </div>
  )
}