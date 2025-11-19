import { useState } from 'react'

/**
 * CheckoutOrderConfirmation
 * Description: order confirmation
 */
export default function CheckoutOrderConfirmation({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="checkoutorderconfirmation" {...props}>
      <div className="checkoutorderconfirmation-content">
        {children}
      </div>
    </div>
  )
}