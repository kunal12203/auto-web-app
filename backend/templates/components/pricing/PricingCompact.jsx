export default function PricingCompact() {
  return (
    <section className="pricing-compact">
      <div className="container">
        <div className="pricing-compact-box">
          <h3>{{PLAN_NAME}}</h3>
          <div className="price-large">${{PLAN_PRICE}}</div>
          <button className="btn-primary">Get Started</button>
        </div>
      </div>
    </section>
  )
}