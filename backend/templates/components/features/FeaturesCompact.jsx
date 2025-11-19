export default function FeaturesCompact() {
  const features = [
    '{{FEATURE_1}}', '{{FEATURE_2}}', '{{FEATURE_3}}',
    '{{FEATURE_4}}', '{{FEATURE_5}}', '{{FEATURE_6}}'
  ]

  return (
    <section className="features-compact">
      <div className="container">
        <div className="features-compact-grid">
          {features.map((f, i) => (
            <div key={i} className="feature-compact-item">
              <span>✓</span>
              <p>{f}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}