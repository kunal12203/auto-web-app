export default function SaaSMetrics() {
  const metrics = [
    { value: '{{METRIC_1_VALUE}}', label: '{{METRIC_1_LABEL}}', trend: '+12%' },
    { value: '{{METRIC_2_VALUE}}', label: '{{METRIC_2_LABEL}}', trend: '+8%' },
    { value: '{{METRIC_3_VALUE}}', label: '{{METRIC_3_LABEL}}', trend: '+15%' }
  ]

  return (
    <section className="saas-metrics">
      <div className="container">
        <div className="metrics-grid">
          {metrics.map((metric, i) => (
            <div key={i} className="metric-card">
              <div className="metric-value">{metric.value}</div>
              <div className="metric-label">{metric.label}</div>
              <span className="metric-trend">{metric.trend}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}