export default function Stats() {
  const stats = [
    { value: '{{STAT_1_VALUE}}', label: '{{STAT_1_LABEL}}', icon: '{{STAT_1_ICON}}' },
    { value: '{{STAT_2_VALUE}}', label: '{{STAT_2_LABEL}}', icon: '{{STAT_2_ICON}}' },
    { value: '{{STAT_3_VALUE}}', label: '{{STAT_3_LABEL}}', icon: '{{STAT_3_ICON}}' },
    { value: '{{STAT_4_VALUE}}', label: '{{STAT_4_LABEL}}', icon: '{{STAT_4_ICON}}' }
  ]

  return (
    <section className="stats stats-grid">
      <div className="container">
        <div className="stats-grid-container">
          {stats.map((stat, index) => (
            <div key={index} className="stat-card">
              <div className="stat-icon">{stat.icon}</div>
              <div className="stat-value">{stat.value}</div>
              <div className="stat-label">{stat.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
