export default function LogoGrid() {
  const logos = [
    '{{LOGO_1}}', '{{LOGO_2}}', '{{LOGO_3}}',
    '{{LOGO_4}}', '{{LOGO_5}}', '{{LOGO_6}}'
  ]

  return (
    <section className="logo-grid">
      <div className="container">
        <h2>{{LOGOS_HEADLINE}}</h2>
        <div className="logos-container">
          {logos.map((logo, i) => (
            <div key={i} className="logo-item">{logo}</div>
          ))}
        </div>
      </div>
    </section>
  )
}