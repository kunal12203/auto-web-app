import { useState } from 'react'

export default function PricingToggle() {
  const [isAnnual, setIsAnnual] = useState(false)

  const plans = [
    { name: 'Basic', monthly: 29, annual: 290 },
    { name: 'Pro', monthly: 59, annual: 590 }
  ]

  return (
    <section className="pricing-toggle">
      <div className="container">
        <div className="billing-toggle">
          <button
            className={!isAnnual ? 'active' : ''}
            onClick={() => setIsAnnual(false)}
          >
            Monthly
          </button>
          <button
            className={isAnnual ? 'active' : ''}
            onClick={() => setIsAnnual(true)}
          >
            Annual
          </button>
        </div>
        <div className="pricing-grid">
          {plans.map((plan, i) => (
            <div key={i} className="pricing-card">
              <h3>{plan.name}</h3>
              <div className="price">
                ${isAnnual ? plan.annual : plan.monthly}
                <span>/{isAnnual ? 'year' : 'month'}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}