import { useState } from 'react'

export default function GallerySlider() {
  const [currentIndex, setCurrentIndex] = useState(0)
  const images = ['{{IMAGE_1}}', '{{IMAGE_2}}', '{{IMAGE_3}}']

  return (
    <section className="gallery-slider">
      <div className="slider-container">
        <button onClick={() => setCurrentIndex((currentIndex - 1 + images.length) % images.length)}>
          ←
        </button>
        <div className="slider-image">{images[currentIndex]}</div>
        <button onClick={() => setCurrentIndex((currentIndex + 1) % images.length)}>
          →
        </button>
      </div>
    </section>
  )
}