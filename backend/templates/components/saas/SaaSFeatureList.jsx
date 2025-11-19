export default function SaaSFeatureList() {
  const features = [
    '{{FEATURE_1}}', '{{FEATURE_2}}', '{{FEATURE_3}}',
    '{{FEATURE_4}}', '{{FEATURE_5}}', '{{FEATURE_6}}'
  ]

  return (
    <section className="saas-feature-list">
      <div className="container">
        <h2>Everything You Need</h2>
        <div className="feature-list-grid">
          {features.map((feature, i) => (
            <div key={i} className="feature-list-item">
              <span className="checkmark">✓</span>
              <p>{feature}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}