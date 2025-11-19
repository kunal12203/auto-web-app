export default function CTA() {
  return (
    <section className="cta cta-boxed">
      <div className="container">
        <div className="cta-box">
          <div className="cta-icon">{{CTA_ICON}}</div>
          <h2>{{CTA_HEADLINE}}</h2>
          <p>{{CTA_SUBHEADLINE}}</p>
          <button className="cta-button">{{CTA_BUTTON_TEXT}}</button>
        </div>
      </div>
    </section>
  )
}
