export default function PricingCardSimple() {
  return (
    <div className="pricing-card-simple">
      <h3>{{PLAN_NAME}}</h3>
      <div className="price">${{PRICE}}<span>/mo</span></div>
      <button className="select-plan">Select Plan</button>
    </div>
  )
}