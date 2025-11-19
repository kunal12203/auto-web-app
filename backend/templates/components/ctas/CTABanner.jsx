export default function CTA() {
  return (
    <section className="cta cta-banner">
      <div className="container">
        <div className="cta-banner-content">
          <div className="cta-text">
            <h3>{{CTA_HEADLINE}}</h3>
            <p>{{CTA_SUBHEADLINE}}</p>
          </div>
          <button className="cta-button">{{CTA_BUTTON_TEXT}}</button>
        </div>
      </div>
    </section>
  )
}
