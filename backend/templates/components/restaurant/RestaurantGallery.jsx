export default function RestaurantGallery() {
  const images = ['{{IMAGE_1}}', '{{IMAGE_2}}', '{{IMAGE_3}}', '{{IMAGE_4}}']

  return (
    <section className="restaurant-gallery">
      <div className="container">
        <h2>Our Ambiance</h2>
        <div className="gallery-grid">
          {images.map((image, i) => (
            <div key={i} className="gallery-photo">{image}</div>
          ))}
        </div>
      </div>
    </section>
  )
}