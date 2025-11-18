export default function Hero() {
  return (
    <section className="hero hero-split" id="home">
      <div className="container">
        <div className="hero-split-container">
          <div className="hero-split-content">
            <h1>{{HERO_HEADLINE}}</h1>
            <p>{{HERO_SUBHEADLINE}}</p>
            <button className="btn-primary">{{CTA_PRIMARY}}</button>
          </div>
          <div className="hero-split-image">
            <div className="hero-image-placeholder">{{HERO_ICON}}</div>
          </div>
        </div>
      </div>
    </section>
  )
}