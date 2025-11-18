export default function VideoGallery() {
  const videos = [
    { title: '{{VIDEO_1_TITLE}}', thumbnail: '{{THUMB_1}}' },
    { title: '{{VIDEO_2_TITLE}}', thumbnail: '{{THUMB_2}}' }
  ]

  return (
    <section className="video-gallery">
      <div className="container">
        <h2>Video Gallery</h2>
        <div className="video-gallery-grid">
          {videos.map((video, i) => (
            <div key={i} className="video-thumbnail">
              <div className="video-thumb">{video.thumbnail}</div>
              <h4>{video.title}</h4>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}