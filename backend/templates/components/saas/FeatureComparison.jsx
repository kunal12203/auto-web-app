export default function FeatureComparison() {
  const features = [
    { name: '{{FEATURE_1}}', basic: true, pro: true, enterprise: true },
    { name: '{{FEATURE_2}}', basic: true, pro: true, enterprise: true },
    { name: '{{FEATURE_3}}', basic: false, pro: true, enterprise: true },
    { name: '{{FEATURE_4}}', basic: false, pro: false, enterprise: true }
  ]

  return (
    <section className="feature-comparison">
      <div className="container">
        <h2>Compare Plans</h2>
        <table className="comparison-table">
          <thead>
            <tr>
              <th>Feature</th>
              <th>Basic</th>
              <th>Pro</th>
              <th>Enterprise</th>
            </tr>
          </thead>
          <tbody>
            {features.map((feature, i) => (
              <tr key={i}>
                <td>{feature.name}</td>
                <td>{feature.basic ? '✓' : '—'}</td>
                <td>{feature.pro ? '✓' : '—'}</td>
                <td>{feature.enterprise ? '✓' : '—'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  )
}