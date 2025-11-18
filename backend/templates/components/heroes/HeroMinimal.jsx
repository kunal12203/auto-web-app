export default function Hero() {
  return (
    <section className="hero hero-minimal" id="home">
      <div className="hero-content">
        <h1>{{HERO_HEADLINE}}</h1>
        <p>{{HERO_SUBHEADLINE}}</p>
        <div className="hero-buttons">
          <button className="btn-primary">{{CTA_PRIMARY}}</button>
        </div>
      </div>
    </section>
  )
}
