import { useState } from 'react'

/**
 * CheckoutAddressForm
 * Description: address form
 */
export default function CheckoutAddressForm({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="checkoutaddressform" {...props}>
      <div className="checkoutaddressform-content">
        {children}
      </div>
    </div>
  )
}