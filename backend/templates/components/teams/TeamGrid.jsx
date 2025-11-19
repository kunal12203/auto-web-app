export default function Team() {
  const team = [
    { name: '{{TEAM_1_NAME}}', role: '{{TEAM_1_ROLE}}', image: '{{TEAM_1_ICON}}', bio: '{{TEAM_1_BIO}}' },
    { name: '{{TEAM_2_NAME}}', role: '{{TEAM_2_ROLE}}', image: '{{TEAM_2_ICON}}', bio: '{{TEAM_2_BIO}}' },
    { name: '{{TEAM_3_NAME}}', role: '{{TEAM_3_ROLE}}', image: '{{TEAM_3_ICON}}', bio: '{{TEAM_3_BIO}}' },
    { name: '{{TEAM_4_NAME}}', role: '{{TEAM_4_ROLE}}', image: '{{TEAM_4_ICON}}', bio: '{{TEAM_4_BIO}}' }
  ]

  return (
    <section className="team team-grid" id="team">
      <div className="container">
        <h2>{{TEAM_HEADLINE}}</h2>
        <p className="section-subtitle">{{TEAM_SUBHEADLINE}}</p>
        <div className="team-grid-container">
          {team.map((member, index) => (
            <div key={index} className="team-card">
              <div className="team-image">{member.image}</div>
              <h3>{member.name}</h3>
              <p className="team-role">{member.role}</p>
              <p className="team-bio">{member.bio}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}