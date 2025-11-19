export default function SaaSChangelog() {
  const updates = [
    { version: '{{VERSION_1}}', date: '{{DATE_1}}', changes: '{{CHANGES_1}}' },
    { version: '{{VERSION_2}}', date: '{{DATE_2}}', changes: '{{CHANGES_2}}' }
  ]

  return (
    <section className="saas-changelog">
      <div className="container">
        <h2>Changelog</h2>
        <div className="changelog-list">
          {updates.map((update, i) => (
            <div key={i} className="changelog-item">
              <div className="changelog-header">
                <strong>Version {update.version}</strong>
                <span>{update.date}</span>
              </div>
              <p>{update.changes}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}