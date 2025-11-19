import { useState } from 'react'

export default function CheckoutSteps() {
  const [step, setStep] = useState(1)

  return (
    <section className="checkout-steps">
      <div className="container">
        <div className="steps-indicator">
          <div className={`step ${step >= 1 ? 'active' : ''}`}>1. Cart</div>
          <div className={`step ${step >= 2 ? 'active' : ''}`}>2. Shipping</div>
          <div className={`step ${step >= 3 ? 'active' : ''}`}>3. Payment</div>
        </div>
        <div className="checkout-content">
          {step === 1 && <div>Cart Items</div>}
          {step === 2 && <div>Shipping Info</div>}
          {step === 3 && <div>Payment Details</div>}
        </div>
      </div>
    </section>
  )
}