export default function Hero() {
  return (
    <section className="hero hero-full-height" id="home">
      <div className="hero-full-content">
        <h1>{{HERO_HEADLINE}}</h1>
        <p>{{HERO_SUBHEADLINE}}</p>
        <button className="btn-primary">{{CTA_PRIMARY}}</button>
        <div className="hero-scroll-indicator">
          <span>Scroll Down ↓</span>
        </div>
      </div>
    </section>
  )
}