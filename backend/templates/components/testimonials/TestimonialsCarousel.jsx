import { useState } from 'react'

export default function TestimonialsCarousel() {
  const [current, setCurrent] = useState(0)
  
  const testimonials = [
    { quote: '{{TESTIMONIAL_1_QUOTE}}', author: '{{TESTIMONIAL_1_AUTHOR}}' },
    { quote: '{{TESTIMONIAL_2_QUOTE}}', author: '{{TESTIMONIAL_2_AUTHOR}}' }
  ]

  return (
    <section className="testimonials-carousel">
      <div className="container">
        <div className="carousel">
          <button onClick={() => setCurrent(Math.max(0, current - 1))}>←</button>
          <div className="testimonial-slide">
            <p>"{testimonials[current].quote}"</p>
            <strong>{testimonials[current].author}</strong>
          </div>
          <button onClick={() => setCurrent(Math.min(testimonials.length - 1, current + 1))}>→</button>
        </div>
      </div>
    </section>
  )
}