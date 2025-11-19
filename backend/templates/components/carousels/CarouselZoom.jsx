import { useState } from 'react'

export default function ZoomCarousel({ items = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [isZoomed, setIsZoomed] = useState(false)

  return (
    <div className="zoom-carousel">
      <div
        className={`carousel-slide ${isZoomed ? 'zoomed' : ''}`}
        onClick={() => setIsZoomed(!isZoomed)}
      >
        <img src={items[currentIndex]?.image} alt={items[currentIndex]?.title} />
      </div>
      <div className="carousel-controls">
        <button onClick={() => setCurrentIndex((currentIndex - 1 + items.length) % items.length)}>‹</button>
        <span>{currentIndex + 1} / {items.length}</span>
        <button onClick={() => setCurrentIndex((currentIndex + 1) % items.length)}>›</button>
      </div>
    </div>
  )
}