export default function ServiceCards() {
  const services = [
    { icon: '{{SERVICE_1_ICON}}', title: '{{SERVICE_1_TITLE}}', description: '{{SERVICE_1_DESC}}' },
    { icon: '{{SERVICE_2_ICON}}', title: '{{SERVICE_2_TITLE}}', description: '{{SERVICE_2_DESC}}' },
    { icon: '{{SERVICE_3_ICON}}', title: '{{SERVICE_3_TITLE}}', description: '{{SERVICE_3_DESC}}' }
  ]

  return (
    <section className="service-cards">
      <div className="container">
        <div className="cards-grid">
          {services.map((service, i) => (
            <div key={i} className="service-card">
              <div className="card-icon">{service.icon}</div>
              <h3>{service.title}</h3>
              <p>{service.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}