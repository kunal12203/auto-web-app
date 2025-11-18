export default function CTA() {
  return (
    <section className="cta cta-with-image">
      <div className="container">
        <div className="cta-content">
          <h2>{{CTA_HEADLINE}}</h2>
          <p>{{CTA_SUBHEADLINE}}</p>
          <button className="cta-button">{{CTA_BUTTON_TEXT}}</button>
        </div>
        <div className="cta-image">
          <div className="cta-placeholder">{{CTA_ICON}}</div>
        </div>
      </div>
    </section>
  )
}
