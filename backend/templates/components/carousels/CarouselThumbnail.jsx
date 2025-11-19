import { useState } from 'react'

export default function ThumbnailCarousel({ items = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0)

  return (
    <div className="thumbnail-carousel">
      <div className="main-slide">
        <img src={items[currentIndex]?.image || '{{MAIN_IMAGE}}'} alt={items[currentIndex]?.title} />
        <div className="slide-info">
          <h3>{items[currentIndex]?.title}</h3>
          <p>{items[currentIndex]?.description}</p>
        </div>
      </div>
      <div className="thumbnails">
        {items.map((item, index) => (
          <button
            key={index}
            className={`thumbnail ${index === currentIndex ? 'active' : ''}`}
            onClick={() => setCurrentIndex(index)}
          >
            <img src={item.thumbnail || item.image} alt={item.title} />
          </button>
        ))}
      </div>
    </div>
  )
}