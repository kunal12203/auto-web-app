export default function ContactCards() {
  const contacts = [
    { icon: '📧', title: 'Email', value: '{{CONTACT_EMAIL}}' },
    { icon: '📞', title: 'Phone', value: '{{CONTACT_PHONE}}' },
    { icon: '📍', title: 'Address', value: '{{CONTACT_ADDRESS}}' }
  ]

  return (
    <section className="contact-cards">
      <div className="container">
        <div className="contact-cards-grid">
          {contacts.map((contact, i) => (
            <div key={i} className="contact-card">
              <div className="contact-icon">{contact.icon}</div>
              <h3>{contact.title}</h3>
              <p>{contact.value}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}