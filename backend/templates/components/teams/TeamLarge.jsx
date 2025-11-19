export default function Team() {
  const team = [
    { name: '{{TEAM_1_NAME}}', role: '{{TEAM_1_ROLE}}', image: '{{TEAM_1_ICON}}', bio: '{{TEAM_1_BIO}}', email: '{{TEAM_1_EMAIL}}' },
    { name: '{{TEAM_2_NAME}}', role: '{{TEAM_2_ROLE}}', image: '{{TEAM_2_ICON}}', bio: '{{TEAM_2_BIO}}', email: '{{TEAM_2_EMAIL}}' },
    { name: '{{TEAM_3_NAME}}', role: '{{TEAM_3_ROLE}}', image: '{{TEAM_3_ICON}}', bio: '{{TEAM_3_BIO}}', email: '{{TEAM_3_EMAIL}}' }
  ]

  return (
    <section className="team team-large" id="team">
      <div className="container">
        <h2>{{TEAM_HEADLINE}}</h2>
        <p className="section-subtitle">{{TEAM_SUBHEADLINE}}</p>
        <div className="team-large-grid">
          {team.map((member, index) => (
            <div key={index} className="team-large-card">
              <div className="team-large-image">{member.image}</div>
              <div className="team-large-info">
                <h3>{member.name}</h3>
                <p className="team-role">{member.role}</p>
                <p className="team-bio">{member.bio}</p>
                <a href={`mailto:${member.email}`} className="team-email">{member.email}</a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}