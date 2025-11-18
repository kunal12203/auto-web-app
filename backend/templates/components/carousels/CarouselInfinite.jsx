import { useState } from 'react'

export default function InfiniteCarousel({ items = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0)
  const extendedItems = [...items, ...items, ...items]

  const next = () => {
    setCurrentIndex((prev) => prev + 1)
    if (currentIndex >= items.length * 2) {
      setTimeout(() => setCurrentIndex(items.length), 300)
    }
  }

  const prev = () => {
    setCurrentIndex((prev) => prev - 1)
    if (currentIndex <= items.length) {
      setTimeout(() => setCurrentIndex(items.length * 2), 300)
    }
  }

  return (
    <div className="infinite-carousel">
      <button onClick={prev}>‹</button>
      <div className="carousel-viewport">
        <div className="carousel-track" style={{ transform: `translateX(-${currentIndex * 100}%)` }}>
          {extendedItems.map((item, index) => (
            <div key={index} className="carousel-slide">{item.content}</div>
          ))}
        </div>
      </div>
      <button onClick={next}>›</button>
    </div>
  )
}