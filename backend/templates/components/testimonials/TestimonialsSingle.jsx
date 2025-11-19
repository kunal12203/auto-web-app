export default function TestimonialsSingle() {
  return (
    <section className="testimonial-single">
      <div className="container">
        <div className="testimonial-box">
          <p className="testimonial-quote-large">
            "{{TESTIMONIAL_QUOTE}}"
          </p>
          <div className="testimonial-author-large">
            <strong>{{TESTIMONIAL_AUTHOR}}</strong>
            <span>{{TESTIMONIAL_ROLE}}</span>
          </div>
        </div>
      </div>
    </section>
  )
}