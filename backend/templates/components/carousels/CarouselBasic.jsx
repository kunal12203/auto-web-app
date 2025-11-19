import { useState } from 'react'

export default function Carousel({ items = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0)

  const defaultItems = [
    { image: '{{CAROUSEL_IMAGE_1}}', title: '{{CAROUSEL_TITLE_1}}', description: '{{CAROUSEL_DESC_1}}' },
    { image: '{{CAROUSEL_IMAGE_2}}', title: '{{CAROUSEL_TITLE_2}}', description: '{{CAROUSEL_DESC_2}}' },
    { image: '{{CAROUSEL_IMAGE_3}}', title: '{{CAROUSEL_TITLE_3}}', description: '{{CAROUSEL_DESC_3}}' }
  ]

  const slides = items.length > 0 ? items : defaultItems

  const next = () => setCurrentIndex((currentIndex + 1) % slides.length)
  const prev = () => setCurrentIndex((currentIndex - 1 + slides.length) % slides.length)

  return (
    <div className="carousel">
      <button className="carousel-btn prev" onClick={prev}>‹</button>
      <div className="carousel-slide">
        <div className="carousel-image">{slides[currentIndex].image}</div>
        <h3>{slides[currentIndex].title}</h3>
        <p>{slides[currentIndex].description}</p>
      </div>
      <button className="carousel-btn next" onClick={next}>›</button>
      <div className="carousel-indicators">
        {slides.map((_, index) => (
          <button
            key={index}
            className={`indicator ${index === currentIndex ? 'active' : ''}`}
            onClick={() => setCurrentIndex(index)}
          />
        ))}
      </div>
    </div>
  )
}