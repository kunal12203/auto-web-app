export default function Stats() {
  const stats = [
    { value: '{{STAT_1_VALUE}}', label: '{{STAT_1_LABEL}}' },
    { value: '{{STAT_2_VALUE}}', label: '{{STAT_2_LABEL}}' },
    { value: '{{STAT_3_VALUE}}', label: '{{STAT_3_LABEL}}' },
    { value: '{{STAT_4_VALUE}}', label: '{{STAT_4_LABEL}}' }
  ]

  return (
    <section className="stats stats-with-headline">
      <div className="container">
        <h2>{{STATS_HEADLINE}}</h2>
        <p className="section-subtitle">{{STATS_SUBHEADLINE}}</p>
        <div className="stats-grid-container">
          {stats.map((stat, index) => (
            <div key={index} className="stat-card">
              <div className="stat-value">{stat.value}</div>
              <div className="stat-label">{stat.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
