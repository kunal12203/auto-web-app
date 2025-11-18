export default function ProductReviews() {
  const reviews = [
    { author: '{{REVIEW_1_AUTHOR}}', rating: '{{REVIEW_1_RATING}}', text: '{{REVIEW_1_TEXT}}', date: '{{REVIEW_1_DATE}}' },
    { author: '{{REVIEW_2_AUTHOR}}', rating: '{{REVIEW_2_RATING}}', text: '{{REVIEW_2_TEXT}}', date: '{{REVIEW_2_DATE}}' },
    { author: '{{REVIEW_3_AUTHOR}}', rating: '{{REVIEW_3_RATING}}', text: '{{REVIEW_3_TEXT}}', date: '{{REVIEW_3_DATE}}' }
  ]

  return (
    <section className="product-reviews">
      <div className="container">
        <h2>Customer Reviews</h2>
        <div className="reviews-list">
          {reviews.map((review, i) => (
            <div key={i} className="review-card">
              <div className="review-header">
                <strong>{review.author}</strong>
                <span>{'⭐'.repeat(parseInt(review.rating))}</span>
              </div>
              <p>{review.text}</p>
              <span className="review-date">{review.date}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}