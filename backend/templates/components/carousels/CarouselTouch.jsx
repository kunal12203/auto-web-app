import { useState, useRef } from 'react'

export default function TouchCarousel({ items = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [touchStart, setTouchStart] = useState(0)
  const [touchEnd, setTouchEnd] = useState(0)

  const handleTouchStart = (e) => {
    setTouchStart(e.touches[0].clientX)
  }

  const handleTouchMove = (e) => {
    setTouchEnd(e.touches[0].clientX)
  }

  const handleTouchEnd = () => {
    if (touchStart - touchEnd > 50) {
      // Swipe left
      setCurrentIndex((prev) => (prev + 1) % items.length)
    }
    if (touchStart - touchEnd < -50) {
      // Swipe right
      setCurrentIndex((prev) => (prev - 1 + items.length) % items.length)
    }
  }

  return (
    <div
      className="touch-carousel"
      onTouchStart={handleTouchStart}
      onTouchMove={handleTouchMove}
      onTouchEnd={handleTouchEnd}
    >
      <div className="carousel-track" style={{ transform: `translateX(-${currentIndex * 100}%)` }}>
        {items.map((item, index) => (
          <div key={index} className="carousel-slide">
            {item.content}
          </div>
        ))}
      </div>
      <div className="carousel-indicators">
        {items.map((_, index) => (
          <span key={index} className={index === currentIndex ? 'active' : ''} />
        ))}
      </div>
    </div>
  )
}