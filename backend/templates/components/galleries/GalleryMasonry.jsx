export default function Gallery() {
  const images = [
    { image: '{{GALLERY_1_ICON}}', category: '{{GALLERY_1_CATEGORY}}' },
    { image: '{{GALLERY_2_ICON}}', category: '{{GALLERY_2_CATEGORY}}' },
    { image: '{{GALLERY_3_ICON}}', category: '{{GALLERY_3_CATEGORY}}' },
    { image: '{{GALLERY_4_ICON}}', category: '{{GALLERY_4_CATEGORY}}' }
  ]

  return (
    <section className="gallery gallery-masonry" id="gallery">
      <div className="container">
        <h2>{{GALLERY_HEADLINE}}</h2>
        <div className="gallery-masonry-container">
          {images.map((item, index) => (
            <div key={index} className="gallery-masonry-item">
              <div className="gallery-image">{item.image}</div>
              <span className="gallery-category">{item.category}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}