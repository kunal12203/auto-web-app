export default function FeaturesAlternating() {
  const features = [
    { title: '{{FEATURE_1_TITLE}}', text: '{{FEATURE_1_TEXT}}', icon: '{{FEATURE_1_ICON}}' },
    { title: '{{FEATURE_2_TITLE}}', text: '{{FEATURE_2_TEXT}}', icon: '{{FEATURE_2_ICON}}' }
  ]

  return (
    <section className="features-alternating">
      <div className="container">
        {features.map((f, i) => (
          <div key={i} className={`feature-row ${i % 2 === 1 ? 'reverse' : ''}`}>
            <div className="feature-content">
              <h3>{f.title}</h3>
              <p>{f.text}</p>
            </div>
            <div className="feature-visual">{f.icon}</div>
          </div>
        ))}
      </div>
    </section>
  )
}