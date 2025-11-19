export default function PartnerLogos() {
  const partners = [
    '{{PARTNER_1}}', '{{PARTNER_2}}', '{{PARTNER_3}}',
    '{{PARTNER_4}}', '{{PARTNER_5}}'
  ]

  return (
    <section className="partner-logos">
      <div className="container">
        <p className="partners-intro">Trusted by</p>
        <div className="partners-grid">
          {partners.map((partner, i) => (
            <div key={i} className="partner-logo">{partner}</div>
          ))}
        </div>
      </div>
    </section>
  )
}