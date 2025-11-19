export default function TimelineVertical() {
  const events = [
    { year: '{{TIMELINE_1_YEAR}}', title: '{{TIMELINE_1_TITLE}}', description: '{{TIMELINE_1_DESC}}' },
    { year: '{{TIMELINE_2_YEAR}}', title: '{{TIMELINE_2_TITLE}}', description: '{{TIMELINE_2_DESC}}' },
    { year: '{{TIMELINE_3_YEAR}}', title: '{{TIMELINE_3_TITLE}}', description: '{{TIMELINE_3_DESC}}' }
  ]

  return (
    <section className="timeline timeline-vertical">
      <div className="container">
        <h2>{{TIMELINE_HEADLINE}}</h2>
        <div className="timeline-container">
          {events.map((event, i) => (
            <div key={i} className="timeline-item">
              <div className="timeline-year">{event.year}</div>
              <div className="timeline-content">
                <h3>{event.title}</h3>
                <p>{event.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}