export default function ContactWithTeam() {
  const team = [
    { name: '{{CONTACT_1_NAME}}', role: '{{CONTACT_1_ROLE}}', email: '{{CONTACT_1_EMAIL}}' },
    { name: '{{CONTACT_2_NAME}}', role: '{{CONTACT_2_ROLE}}', email: '{{CONTACT_2_EMAIL}}' }
  ]

  return (
    <section className="contact-with-team">
      <div className="container">
        <h2>Contact Our Team</h2>
        <div className="team-contact-grid">
          {team.map((member, i) => (
            <div key={i} className="team-contact-card">
              <h3>{member.name}</h3>
              <p>{member.role}</p>
              <a href={`mailto:${member.email}`}>{member.email}</a>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}