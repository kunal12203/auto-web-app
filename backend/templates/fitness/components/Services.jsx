export default function Services() {
  const services = [
    {
      icon: '💪',
      title: 'Personal Training',
      description: 'One-on-one coaching tailored to your goals'
    },
    {
      icon: '🤸',
      title: 'Group Classes',
      description: 'High-energy workouts with motivated community'
    },
    {
      icon: '🧘',
      title: 'Yoga & Pilates',
      description: 'Flexibility and mindfulness training'
    },
    {
      icon: '🏃',
      title: 'Cardio Zone',
      description: 'State-of-the-art cardio equipment'
    }
  ]

  return (
    <section className="services" id="services">
      <h2>Our Services</h2>
      <p className="section-subtitle">Everything you need to achieve your fitness goals</p>
      <div className="services-grid">
        {services.map((service, index) => (
          <div key={index} className="service-card">
            <div className="service-icon">{service.icon}</div>
            <h3>{service.title}</h3>
            <p>{service.description}</p>
          </div>
        ))}
      </div>
    </section>
  )
}
