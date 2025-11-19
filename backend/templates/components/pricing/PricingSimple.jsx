export default function PricingSimple() {
  const plans = [
    { name: '{{PLAN_1_NAME}}', price: '{{PLAN_1_PRICE}}' },
    { name: '{{PLAN_2_NAME}}', price: '{{PLAN_2_PRICE}}' }
  ]

  return (
    <section className="pricing-simple">
      <div className="container">
        <h2>Simple Pricing</h2>
        <div className="pricing-row">
          {plans.map((plan, i) => (
            <div key={i} className="pricing-item-simple">
              <h3>{plan.name}</h3>
              <div className="price-simple">${plan.price}</div>
              <button>Choose Plan</button>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}