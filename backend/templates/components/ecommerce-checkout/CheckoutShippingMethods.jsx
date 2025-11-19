import { useState } from 'react'

/**
 * CheckoutShippingMethods
 * Description: shipping methods
 */
export default function CheckoutShippingMethods({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="checkoutshippingmethods" {...props}>
      <div className="checkoutshippingmethods-content">
        {children}
      </div>
    </div>
  )
}