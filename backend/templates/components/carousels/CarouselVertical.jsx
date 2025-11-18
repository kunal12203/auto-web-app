import { useState } from 'react'

export default function VerticalCarousel({ items = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0)

  const next = () => setCurrentIndex((currentIndex + 1) % items.length)
  const prev = () => setCurrentIndex((currentIndex - 1 + items.length) % items.length)

  return (
    <div className="vertical-carousel">
      <button className="carousel-btn up" onClick={prev}>▲</button>
      <div className="carousel-track" style={{ transform: `translateY(-${currentIndex * 100}%)` }}>
        {items.map((item, index) => (
          <div key={index} className="carousel-slide">
            {item.content}
          </div>
        ))}
      </div>
      <button className="carousel-btn down" onClick={next}>▼</button>
    </div>
  )
}