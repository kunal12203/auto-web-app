import { useState } from 'react'

export default function MultiItemCarousel({ items = [], itemsPerSlide = 3 }) {
  const [currentIndex, setCurrentIndex] = useState(0)

  const totalSlides = Math.ceil(items.length / itemsPerSlide)

  const next = () => setCurrentIndex((currentIndex + 1) % totalSlides)
  const prev = () => setCurrentIndex((currentIndex - 1 + totalSlides) % totalSlides)

  const visibleItems = items.slice(
    currentIndex * itemsPerSlide,
    (currentIndex + 1) * itemsPerSlide
  )

  return (
    <div className="multi-item-carousel">
      <button className="carousel-btn prev" onClick={prev}>‹</button>
      <div className="carousel-items">
        {visibleItems.map((item, index) => (
          <div key={index} className="carousel-item">
            {item.content}
          </div>
        ))}
      </div>
      <button className="carousel-btn next" onClick={next}>›</button>
    </div>
  )
}