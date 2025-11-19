export default function Hero() {
  return (
    <section className="hero hero-gradient" id="home">
      <div className="hero-gradient-bg">
        <div className="container">
          <h1>{{HERO_HEADLINE}}</h1>
          <p>{{HERO_SUBHEADLINE}}</p>
          <div className="hero-buttons">
            <button className="btn-primary">{{CTA_PRIMARY}}</button>
            <button className="btn-secondary">{{CTA_SECONDARY}}</button>
          </div>
        </div>
      </div>
    </section>
  )
}