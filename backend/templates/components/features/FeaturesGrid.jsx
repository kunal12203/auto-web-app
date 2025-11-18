export default function Features() {
  const features = [
    {
      icon: '{{FEATURE_1_ICON}}',
      title: '{{FEATURE_1_TITLE}}',
      description: '{{FEATURE_1_DESC}}'
    },
    {
      icon: '{{FEATURE_2_ICON}}',
      title: '{{FEATURE_2_TITLE}}',
      description: '{{FEATURE_2_DESC}}'
    },
    {
      icon: '{{FEATURE_3_ICON}}',
      title: '{{FEATURE_3_TITLE}}',
      description: '{{FEATURE_3_DESC}}'
    },
    {
      icon: '{{FEATURE_4_ICON}}',
      title: '{{FEATURE_4_TITLE}}',
      description: '{{FEATURE_4_DESC}}'
    }
  ]

  return (
    <section className="features" id="services">
      <div className="container">
        <h2>{{FEATURES_HEADLINE}}</h2>
        <p className="section-subtitle">{{FEATURES_SUBHEADLINE}}</p>
        <div className="features-grid">
          {features.map((feature, index) => (
            <div key={index} className="feature-card">
              <div className="feature-icon">{feature.icon}</div>
              <h3>{feature.title}</h3>
              <p>{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
