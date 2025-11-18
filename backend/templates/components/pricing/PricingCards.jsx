export default function Pricing() {
  const plans = [
    {
      name: '{{PLAN_1_NAME}}',
      price: '{{PLAN_1_PRICE}}',
      period: '{{PLAN_1_PERIOD}}',
      features: [
        '{{PLAN_1_FEATURE_1}}',
        '{{PLAN_1_FEATURE_2}}',
        '{{PLAN_1_FEATURE_3}}',
        '{{PLAN_1_FEATURE_4}}'
      ],
      featured: false
    },
    {
      name: '{{PLAN_2_NAME}}',
      price: '{{PLAN_2_PRICE}}',
      period: '{{PLAN_2_PERIOD}}',
      features: [
        '{{PLAN_2_FEATURE_1}}',
        '{{PLAN_2_FEATURE_2}}',
        '{{PLAN_2_FEATURE_3}}',
        '{{PLAN_2_FEATURE_4}}',
        '{{PLAN_2_FEATURE_5}}'
      ],
      featured: true
    },
    {
      name: '{{PLAN_3_NAME}}',
      price: '{{PLAN_3_PRICE}}',
      period: '{{PLAN_3_PERIOD}}',
      features: [
        '{{PLAN_3_FEATURE_1}}',
        '{{PLAN_3_FEATURE_2}}',
        '{{PLAN_3_FEATURE_3}}',
        '{{PLAN_3_FEATURE_4}}',
        '{{PLAN_3_FEATURE_5}}',
        '{{PLAN_3_FEATURE_6}}'
      ],
      featured: false
    }
  ]

  return (
    <section className="pricing" id="pricing">
      <div className="container">
        <h2>{{PRICING_HEADLINE}}</h2>
        <p className="section-subtitle">{{PRICING_SUBHEADLINE}}</p>
        <div className="pricing-grid">
          {plans.map((plan, index) => (
            <div key={index} className={`pricing-card ${plan.featured ? 'featured' : ''}`}>
              {plan.featured && <span className="badge">Most Popular</span>}
              <h3>{plan.name}</h3>
              <div className="price">
                <span className="amount">${plan.price}</span>
                <span className="period">/{plan.period}</span>
              </div>
              <ul className="features">
                {plan.features.map((feature, i) => (
                  <li key={i}>✓ {feature}</li>
                ))}
              </ul>
              <button className="cta-button">Choose Plan</button>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
