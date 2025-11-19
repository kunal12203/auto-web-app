export default function Team() {
  const team = [
    { name: '{{TEAM_1_NAME}}', role: '{{TEAM_1_ROLE}}', image: '{{TEAM_1_ICON}}', social: { linkedin: '#', twitter: '#' } },
    { name: '{{TEAM_2_NAME}}', role: '{{TEAM_2_ROLE}}', image: '{{TEAM_2_ICON}}', social: { linkedin: '#', twitter: '#' } },
    { name: '{{TEAM_3_NAME}}', role: '{{TEAM_3_ROLE}}', image: '{{TEAM_3_ICON}}', social: { linkedin: '#', twitter: '#' } }
  ]

  return (
    <section className="team team-with-social" id="team">
      <div className="container">
        <h2>{{TEAM_HEADLINE}}</h2>
        <div className="team-grid-container">
          {team.map((member, index) => (
            <div key={index} className="team-card-social">
              <div className="team-image">{member.image}</div>
              <h3>{member.name}</h3>
              <p className="team-role">{member.role}</p>
              <div className="team-social">
                <a href={member.social.linkedin}>LinkedIn</a>
                <a href={member.social.twitter}>Twitter</a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}