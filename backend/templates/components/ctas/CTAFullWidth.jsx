export default function CTA() {
  return (
    <section className="cta cta-fullwidth">
      <div className="cta-overlay">
        <div className="container">
          <h2>{{CTA_HEADLINE}}</h2>
          <p>{{CTA_SUBHEADLINE}}</p>
          <div className="cta-buttons">
            <button className="btn-primary">{{CTA_PRIMARY_BUTTON}}</button>
            <button className="btn-secondary">{{CTA_SECONDARY_BUTTON}}</button>
          </div>
        </div>
      </div>
    </section>
  )
}
