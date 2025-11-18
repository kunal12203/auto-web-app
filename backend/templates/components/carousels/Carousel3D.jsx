import { useState } from 'react'

export default function Carousel3D({ items = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0)

  const getTransform = (index) => {
    const diff = index - currentIndex
    const angle = diff * 60
    const translateZ = Math.abs(diff) === 0 ? 200 : 0
    return `rotateY(${angle}deg) translateZ(${translateZ}px)`
  }

  return (
    <div className="carousel-3d-container">
      <div className="carousel-3d">
        {items.map((item, index) => (
          <div
            key={index}
            className={`carousel-3d-item ${index === currentIndex ? 'active' : ''}`}
            style={{ transform: getTransform(index) }}
            onClick={() => setCurrentIndex(index)}
          >
            {item.content}
          </div>
        ))}
      </div>
      <div className="carousel-controls">
        <button onClick={() => setCurrentIndex((currentIndex - 1 + items.length) % items.length)}>‹</button>
        <button onClick={() => setCurrentIndex((currentIndex + 1) % items.length)}>›</button>
      </div>
    </div>
  )
}