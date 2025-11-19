export default function Team() {
  const team = [
    { name: '{{TEAM_1_NAME}}', role: '{{TEAM_1_ROLE}}' },
    { name: '{{TEAM_2_NAME}}', role: '{{TEAM_2_ROLE}}' },
    { name: '{{TEAM_3_NAME}}', role: '{{TEAM_3_ROLE}}' }
  ]

  return (
    <section className="team team-minimal" id="team">
      <div className="container">
        <h2>{{TEAM_HEADLINE}}</h2>
        <div className="team-list">
          {team.map((member, index) => (
            <div key={index} className="team-item-minimal">
              <h3>{member.name}</h3>
              <p>{member.role}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}