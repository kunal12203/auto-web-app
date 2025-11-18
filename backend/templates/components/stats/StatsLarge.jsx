export default function Stats() {
  const stats = [
    { value: '{{STAT_1_VALUE}}', label: '{{STAT_1_LABEL}}', description: '{{STAT_1_DESC}}' },
    { value: '{{STAT_2_VALUE}}', label: '{{STAT_2_LABEL}}', description: '{{STAT_2_DESC}}' },
    { value: '{{STAT_3_VALUE}}', label: '{{STAT_3_LABEL}}', description: '{{STAT_3_DESC}}' }
  ]

  return (
    <section className="stats stats-large">
      <div className="container">
        <div className="stats-large-grid">
          {stats.map((stat, index) => (
            <div key={index} className="stat-large-card">
              <div className="stat-value-large">{stat.value}</div>
              <div className="stat-label-large">{stat.label}</div>
              <p className="stat-description">{stat.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
