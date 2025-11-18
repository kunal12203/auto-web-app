export default function Stats() {
  const stats = [
    { value: '{{STAT_1_VALUE}}', label: '{{STAT_1_LABEL}}', prefix: '{{STAT_1_PREFIX}}', suffix: '{{STAT_1_SUFFIX}}' },
    { value: '{{STAT_2_VALUE}}', label: '{{STAT_2_LABEL}}', prefix: '{{STAT_2_PREFIX}}', suffix: '{{STAT_2_SUFFIX}}' },
    { value: '{{STAT_3_VALUE}}', label: '{{STAT_3_LABEL}}', prefix: '{{STAT_3_PREFIX}}', suffix: '{{STAT_3_SUFFIX}}' },
    { value: '{{STAT_4_VALUE}}', label: '{{STAT_4_LABEL}}', prefix: '{{STAT_4_PREFIX}}', suffix: '{{STAT_4_SUFFIX}}' }
  ]

  return (
    <section className="stats stats-counter">
      <div className="container">
        <h2>{{STATS_HEADLINE}}</h2>
        <div className="stats-counter-grid">
          {stats.map((stat, index) => (
            <div key={index} className="stat-counter-item">
              <div className="stat-counter-value">
                <span className="stat-prefix">{stat.prefix}</span>
                {stat.value}
                <span className="stat-suffix">{stat.suffix}</span>
              </div>
              <div className="stat-counter-label">{stat.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
