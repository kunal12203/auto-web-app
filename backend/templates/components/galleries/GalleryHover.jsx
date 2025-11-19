export default function GalleryHover() {
  const items = [
    { image: '{{IMAGE_1}}', title: '{{TITLE_1}}', description: '{{DESC_1}}' },
    { image: '{{IMAGE_2}}', title: '{{TITLE_2}}', description: '{{DESC_2}}' }
  ]

  return (
    <section className="gallery-hover">
      <div className="container">
        <div className="gallery-hover-grid">
          {items.map((item, i) => (
            <div key={i} className="gallery-hover-item">
              <div className="gallery-image">{item.image}</div>
              <div className="gallery-overlay">
                <h3>{item.title}</h3>
                <p>{item.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}