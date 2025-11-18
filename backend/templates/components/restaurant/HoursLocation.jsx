export default function HoursLocation() {
  const hours = [
    { day: 'Monday - Friday', time: '{{HOURS_WEEKDAY}}' },
    { day: 'Saturday', time: '{{HOURS_SATURDAY}}' },
    { day: 'Sunday', time: '{{HOURS_SUNDAY}}' }
  ]

  return (
    <section className="hours-location">
      <div className="container">
        <div className="hours-grid">
          <div className="hours">
            <h3>Hours</h3>
            {hours.map((item, i) => (
              <div key={i} className="hours-row">
                <span>{item.day}</span>
                <span>{item.time}</span>
              </div>
            ))}
          </div>
          <div className="location">
            <h3>Location</h3>
            <p>📍 {{CONTACT_ADDRESS}}</p>
            <p>📞 {{CONTACT_PHONE}}</p>
          </div>
        </div>
      </div>
    </section>
  )
}