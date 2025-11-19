import { useState } from 'react'

/**
 * CheckoutOrderSummary
 * Description: order summary
 */
export default function CheckoutOrderSummary({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="checkoutordersummary" {...props}>
      <div className="checkoutordersummary-content">
        {children}
      </div>
    </div>
  )
}