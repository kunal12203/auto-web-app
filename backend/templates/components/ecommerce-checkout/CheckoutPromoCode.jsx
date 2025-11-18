import { useState } from 'react'

/**
 * CheckoutPromoCode
 * Description: promo code input
 */
export default function CheckoutPromoCode({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="checkoutpromocode" {...props}>
      <div className="checkoutpromocode-content">
        {children}
      </div>
    </div>
  )
}