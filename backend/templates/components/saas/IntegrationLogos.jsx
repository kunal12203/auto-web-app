export default function IntegrationLogos() {
  const integrations = [
    '{{INTEGRATION_1}}', '{{INTEGRATION_2}}', '{{INTEGRATION_3}}',
    '{{INTEGRATION_4}}', '{{INTEGRATION_5}}', '{{INTEGRATION_6}}'
  ]

  return (
    <section className="integrations">
      <div className="container">
        <h2>Integrates With Your Favorite Tools</h2>
        <div className="integration-grid">
          {integrations.map((integration, i) => (
            <div key={i} className="integration-logo">
              {integration}
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}