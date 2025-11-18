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
    }
  ]

  return (
    <section className="features features-list" id="services">
      <div className="container">
        <h2>{{FEATURES_HEADLINE}}</h2>
        <p className="section-subtitle">{{FEATURES_SUBHEADLINE}}</p>
        <div className="features-list-container">
          {features.map((feature, index) => (
            <div key={index} className="feature-item">
              <div className="feature-icon">{feature.icon}</div>
              <div className="feature-content">
                <h3>{feature.title}</h3>
                <p>{feature.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
