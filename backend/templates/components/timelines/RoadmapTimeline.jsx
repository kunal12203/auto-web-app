export default function RoadmapTimeline() {
  const milestones = [
    { quarter: 'Q1 2024', title: '{{MILESTONE_1}}', status: 'completed' },
    { quarter: 'Q2 2024', title: '{{MILESTONE_2}}', status: 'in-progress' },
    { quarter: 'Q3 2024', title: '{{MILESTONE_3}}', status: 'planned' }
  ]

  return (
    <section className="roadmap-timeline">
      <div className="container">
        <h2>Product Roadmap</h2>
        <div className="roadmap">
          {milestones.map((milestone, i) => (
            <div key={i} className={`roadmap-item ${milestone.status}`}>
              <div className="roadmap-quarter">{milestone.quarter}</div>
              <h3>{milestone.title}</h3>
              <span className="status-badge">{milestone.status}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}