export default function Testimonials() {
  const testimonials = [
    {
      quote: "Best gym I've ever joined! The trainers are knowledgeable and the community is amazing.",
      name: 'Sarah Johnson',
      role: 'Member for 2 years'
    },
    {
      quote: "Lost 30 pounds and gained so much confidence. The personal training program changed my life!",
      name: 'Mike Chen',
      role: 'Member for 1 year'
    },
    {
      quote: "The group classes are incredibly fun and motivating. I actually look forward to working out now!",
      name: 'Emily Rodriguez',
      role: 'Member for 6 months'
    }
  ]

  return (
    <section className="testimonials" id="testimonials">
      <h2>What Our Members Say</h2>
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
    </section>
  )
}
