export default function VideoBackground() {
  return (
    <section className="video-background">
      <div className="video-bg-overlay">
        <div className="video-bg-content">
          <h1>{{HEADLINE}}</h1>
          <button className="btn-primary">{{CTA}}</button>
        </div>
      </div>
    </section>
  )
}