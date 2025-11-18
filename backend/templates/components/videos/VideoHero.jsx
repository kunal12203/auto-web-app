export default function VideoHero() {
  return (
    <section className="video-hero">
      <div className="video-container">
        <div className="video-placeholder">▶️ Video</div>
        <div className="video-overlay">
          <h1>{{VIDEO_HEADLINE}}</h1>
          <button className="play-button">Play</button>
        </div>
      </div>
    </section>
  )
}