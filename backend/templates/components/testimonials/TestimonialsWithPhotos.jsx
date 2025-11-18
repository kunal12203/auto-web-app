export default function TestimonialsWithPhotos() {
  const testimonials = [
    { quote: '{{TESTIMONIAL_1_QUOTE}}', author: '{{TESTIMONIAL_1_AUTHOR}}', photo: '{{PHOTO_1}}' },
    { quote: '{{TESTIMONIAL_2_QUOTE}}', author: '{{TESTIMONIAL_2_AUTHOR}}', photo: '{{PHOTO_2}}' }
  ]

  return (
    <section className="testimonials-with-photos">
      <div className="container">
        <div className="testimonials-grid-photos">
          {testimonials.map((t, i) => (
            <div key={i} className="testimonial-photo-card">
              <div className="testimonial-photo">{t.photo}</div>
              <p>"{t.quote}"</p>
              <strong>{t.author}</strong>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}