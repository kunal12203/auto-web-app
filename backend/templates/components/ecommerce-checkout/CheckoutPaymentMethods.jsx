import { useState } from 'react'

/**
 * CheckoutPaymentMethods
 * Description: payment methods
 */
export default function CheckoutPaymentMethods({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="checkoutpaymentmethods" {...props}>
      <div className="checkoutpaymentmethods-content">
        {children}
      </div>
    </div>
  )
}