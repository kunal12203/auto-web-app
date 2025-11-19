export default function MilestoneTimeline() {
  const milestones = [
    { date: '{{DATE_1}}', milestone: '{{MILESTONE_1}}', icon: '{{ICON_1}}' },
    { date: '{{DATE_2}}', milestone: '{{MILESTONE_2}}', icon: '{{ICON_2}}' }
  ]

  return (
    <section className="milestone-timeline">
      <div className="container">
        <h2>Our Journey</h2>
        <div className="milestones">
          {milestones.map((m, i) => (
            <div key={i} className="milestone">
              <div className="milestone-icon">{m.icon}</div>
              <div className="milestone-content">
                <strong>{m.date}</strong>
                <p>{m.milestone}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}