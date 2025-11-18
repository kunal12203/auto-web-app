export default function Hero() {
  return (
    <section className="hero hero-video" id="home">
      <div className="hero-video-bg">
        <div className="hero-overlay">
          <div className="hero-content">
            <h1>{{HERO_HEADLINE}}</h1>
            <p>{{HERO_SUBHEADLINE}}</p>
            <div className="hero-buttons">
              <button className="btn-primary">{{CTA_PRIMARY}}</button>
              <button className="btn-secondary">{{CTA_SECONDARY}}</button>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}