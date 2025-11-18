export default function Testimonials() {
  const testimonials = [
    {
      quote: '{{TESTIMONIAL_1_QUOTE}}',
      name: '{{TESTIMONIAL_1_NAME}}',
      role: '{{TESTIMONIAL_1_ROLE}}'
    },
    {
      quote: '{{TESTIMONIAL_2_QUOTE}}',
      name: '{{TESTIMONIAL_2_NAME}}',
      role: '{{TESTIMONIAL_2_ROLE}}'
    },
    {
      quote: '{{TESTIMONIAL_3_QUOTE}}',
      name: '{{TESTIMONIAL_3_NAME}}',
      role: '{{TESTIMONIAL_3_ROLE}}'
    }
  ]

  return (
    <section className="testimonials" id="testimonials">
      <div className="container">
        <h2>{{TESTIMONIALS_HEADLINE}}</h2>
        <div className="testimonials-grid">
          {testimonials.map((testimonial, index) => (
            <div key={index} className="testimonial-card">
              <p className="quote">"{testimonial.quote}"</p>
              <div className="author">
                <strong>{testimonial.name}</strong>
                <span>{testimonial.role}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
