export default function Gallery() {
  const images = [
    { title: '{{GALLERY_1_TITLE}}', image: '{{GALLERY_1_ICON}}' },
    { title: '{{GALLERY_2_TITLE}}', image: '{{GALLERY_2_ICON}}' },
    { title: '{{GALLERY_3_TITLE}}', image: '{{GALLERY_3_ICON}}' },
    { title: '{{GALLERY_4_TITLE}}', image: '{{GALLERY_4_ICON}}' },
    { title: '{{GALLERY_5_TITLE}}', image: '{{GALLERY_5_ICON}}' },
    { title: '{{GALLERY_6_TITLE}}', image: '{{GALLERY_6_ICON}}' }
  ]

  return (
    <section className="gallery gallery-grid" id="gallery">
      <div className="container">
        <h2>{{GALLERY_HEADLINE}}</h2>
        <div className="gallery-grid-container">
          {images.map((item, index) => (
            <div key={index} className="gallery-item">
              <div className="gallery-image">{item.image}</div>
              <h3>{item.title}</h3>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}