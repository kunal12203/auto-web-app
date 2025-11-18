export default function TimelineHorizontal() {
  const events = [
    { year: '{{YEAR_1}}', event: '{{EVENT_1}}' },
    { year: '{{YEAR_2}}', event: '{{EVENT_2}}' },
    { year: '{{YEAR_3}}', event: '{{EVENT_3}}' }
  ]

  return (
    <section className="timeline-horizontal">
      <div className="container">
        <div className="timeline-horiz">
          {events.map((event, i) => (
            <div key={i} className="timeline-horiz-item">
              <div className="timeline-year">{event.year}</div>
              <p>{event.event}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}