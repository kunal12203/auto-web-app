export default function SaaSStatusPage() {
  const services = [
    { name: '{{SERVICE_1}}', status: 'operational' },
    { name: '{{SERVICE_2}}', status: 'operational' },
    { name: '{{SERVICE_3}}', status: 'degraded' }
  ]

  return (
    <section className="saas-status">
      <div className="container">
        <h2>System Status</h2>
        <div className="status-list">
          {services.map((service, i) => (
            <div key={i} className="status-item">
              <span>{service.name}</span>
              <span className={`status-badge ${service.status}`}>
                {service.status}
              </span>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}