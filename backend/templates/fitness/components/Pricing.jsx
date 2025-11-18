export default function Pricing() {
  const plans = [
    {
      name: 'Basic',
      price: 29,
      period: 'month',
      features: [
        'Access to gym equipment',
        'Locker room access',
        'Mobile app access',
        'Basic workout plans'
      ],
      featured: false
    },
    {
      name: 'Premium',
      price: 59,
      period: 'month',
      features: [
        'All Basic features',
        'Unlimited group classes',
        'Personal trainer sessions (2/month)',
        'Nutrition guidance',
        'Priority booking'
      ],
      featured: true
    },
    {
      name: 'Elite',
      price: 99,
      period: 'month',
      features: [
        'All Premium features',
        'Unlimited personal training',
        'Custom meal plans',
        '24/7 gym access',
        'Guest passes (5/month)'
      ],
      featured: false
    }
  ]

  return (
    <section className="pricing" id="pricing">
      <h2>Membership Plans</h2>
      <p className="section-subtitle">Choose the perfect plan for your fitness journey</p>
      <div className="pricing-grid">
        {plans.map((plan, index) => (
          <div key={index} className={`pricing-card ${plan.featured ? 'featured' : ''}`}>
            {plan.featured && <div className="badge">Most Popular</div>}
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
            <button className="btn-primary">Choose Plan</button>
          </div>
        ))}
      </div>
    </section>
  )
}
