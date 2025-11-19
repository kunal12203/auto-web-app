import { useState } from 'react'

/**
 * CheckoutSteps
 * Description: checkout steps
 */
export default function CheckoutSteps({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="checkoutsteps" {...props}>
      <div className="checkoutsteps-content">
        {children}
      </div>
    </div>
  )
}