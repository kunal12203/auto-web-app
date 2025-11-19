export default function FeaturesWithIcons() {
  const features = [
    { icon: '{{FEATURE_1_ICON}}', title: '{{FEATURE_1_TITLE}}', text: '{{FEATURE_1_TEXT}}' },
    { icon: '{{FEATURE_2_ICON}}', title: '{{FEATURE_2_TITLE}}', text: '{{FEATURE_2_TEXT}}' },
    { icon: '{{FEATURE_3_ICON}}', title: '{{FEATURE_3_TITLE}}', text: '{{FEATURE_3_TEXT}}' }
  ]

  return (
    <section className="features-with-icons">
      <div className="container">
        <h2>{{FEATURES_HEADLINE}}</h2>
        <div className="features-flex">
          {features.map((f, i) => (
            <div key={i} className="feature-item-icon">
              <div className="feature-icon-large">{f.icon}</div>
              <h3>{f.title}</h3>
              <p>{f.text}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}