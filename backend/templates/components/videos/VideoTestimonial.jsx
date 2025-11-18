export default function VideoTestimonial() {
  const testimonials = [
    { name: '{{TESTIMONIAL_1_NAME}}', role: '{{TESTIMONIAL_1_ROLE}}', videoId: '{{VIDEO_1}}' },
    { name: '{{TESTIMONIAL_2_NAME}}', role: '{{TESTIMONIAL_2_ROLE}}', videoId: '{{VIDEO_2}}' }
  ]

  return (
    <section className="video-testimonials">
      <div className="container">
        <h2>Customer Stories</h2>
        <div className="video-testimonials-grid">
          {testimonials.map((item, i) => (
            <div key={i} className="video-testimonial-card">
              <div className="video-thumbnail">▶️</div>
              <h3>{item.name}</h3>
              <p>{item.role}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}