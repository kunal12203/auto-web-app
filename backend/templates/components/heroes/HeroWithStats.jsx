export default function Hero() {
  const stats = [
    { value: '{{STAT_1_VALUE}}', label: '{{STAT_1_LABEL}}' },
    { value: '{{STAT_2_VALUE}}', label: '{{STAT_2_LABEL}}' },
    { value: '{{STAT_3_VALUE}}', label: '{{STAT_3_LABEL}}' }
  ]

  return (
    <section className="hero hero-with-stats" id="home">
      <div className="container">
        <h1>{{HERO_HEADLINE}}</h1>
        <p>{{HERO_SUBHEADLINE}}</p>
        <div className="hero-stats">
          {stats.map((stat, i) => (
            <div key={i} className="hero-stat">
              <div className="stat-value">{stat.value}</div>
              <div className="stat-label">{stat.label}</div>
            </div>
          ))}
        </div>
        <button className="btn-primary">{{CTA_PRIMARY}}</button>
      </div>
    </section>
  )
}