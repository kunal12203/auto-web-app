export default function CTA() {
  const stats = [
    { value: '{{STAT_1_VALUE}}', label: '{{STAT_1_LABEL}}' },
    { value: '{{STAT_2_VALUE}}', label: '{{STAT_2_LABEL}}' },
    { value: '{{STAT_3_VALUE}}', label: '{{STAT_3_LABEL}}' }
  ]

  return (
    <section className="cta cta-with-stats">
      <div className="container">
        <h2>{{CTA_HEADLINE}}</h2>
        <p>{{CTA_SUBHEADLINE}}</p>
        <div className="cta-stats">
          {stats.map((stat, index) => (
            <div key={index} className="stat-item">
              <div className="stat-value">{stat.value}</div>
              <div className="stat-label">{stat.label}</div>
            </div>
          ))}
        </div>
        <button className="cta-button">{{CTA_BUTTON_TEXT}}</button>
      </div>
    </section>
  )
}
