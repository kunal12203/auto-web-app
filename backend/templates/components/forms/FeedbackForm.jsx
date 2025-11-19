import { useState } from 'react'

export default function FeedbackForm() {
  const [rating, setRating] = useState(5)

  return (
    <section className="feedback-form">
      <div className="container">
        <h2>We'd Love Your Feedback</h2>
        <form onSubmit={(e) => e.preventDefault()}>
          <div className="rating-selector">
            <label>Rating:</label>
            {[1,2,3,4,5].map(n => (
              <button
                key={n}
                type="button"
                className={n <= rating ? 'active' : ''}
                onClick={() => setRating(n)}
              >
                ⭐
              </button>
            ))}
          </div>
          <textarea placeholder="Your feedback..." required />
          <button type="submit" className="btn-primary">Submit Feedback</button>
        </form>
      </div>
    </section>
  )
}