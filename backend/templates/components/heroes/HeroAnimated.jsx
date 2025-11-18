export default function Hero() {
  return (
    <section className="hero hero-animated" id="home">
      <div className="container">
        <div className="hero-animated-content">
          <h1 className="hero-fade-in">{{HERO_HEADLINE}}</h1>
          <p className="hero-fade-in-delay">{{HERO_SUBHEADLINE}}</p>
          <div className="hero-buttons hero-fade-in-delay-2">
            <button className="btn-primary">{{CTA_PRIMARY}}</button>
          </div>
        </div>
      </div>
    </section>
  )
}