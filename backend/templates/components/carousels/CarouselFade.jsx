import { useState, useEffect } from 'react'

export default function FadeCarousel({ items = [], duration = 4000 }) {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [fadeClass, setFadeClass] = useState('fade-in')

  useEffect(() => {
    const timer = setInterval(() => {
      setFadeClass('fade-out')
      setTimeout(() => {
        setCurrentIndex((prev) => (prev + 1) % items.length)
        setFadeClass('fade-in')
      }, 300)
    }, duration)

    return () => clearInterval(timer)
  }, [items.length, duration])

  return (
    <div className="fade-carousel">
      <div className={`carousel-slide ${fadeClass}`}>
        {items[currentIndex]?.content}
      </div>
    </div>
  )
}