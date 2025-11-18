export default function Stats() {
  const stats = [
    { value: '{{STAT_1_VALUE}}', label: '{{STAT_1_LABEL}}' },
    { value: '{{STAT_2_VALUE}}', label: '{{STAT_2_LABEL}}' },
    { value: '{{STAT_3_VALUE}}', label: '{{STAT_3_LABEL}}' }
  ]

  return (
    <section className="stats stats-minimal">
      <div className="container">
        <div className="stats-row">
          {stats.map((stat, index) => (
            <div key={index} className="stat-item-minimal">
              <div className="stat-value">{stat.value}</div>
              <div className="stat-label">{stat.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
