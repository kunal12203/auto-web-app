import { useState } from 'react'

export default function GalleryLightbox() {
  const [selectedImage, setSelectedImage] = useState(null)

  return (
    <section className="gallery-lightbox">
      <div className="container">
        <div className="gallery-grid">
          {['{{IMAGE_1}}', '{{IMAGE_2}}', '{{IMAGE_3}}'].map((img, i) => (
            <div key={i} className="gallery-item" onClick={() => setSelectedImage(img)}>
              {img}
            </div>
          ))}
        </div>
      </div>
      {selectedImage && (
        <div className="lightbox" onClick={() => setSelectedImage(null)}>
          <div className="lightbox-image">{selectedImage}</div>
        </div>
      )}
    </section>
  )
}