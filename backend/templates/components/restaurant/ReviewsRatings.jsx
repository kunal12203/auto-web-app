export default function ReviewsRatings() {
  return (
    <section className="reviews-ratings">
      <div className="container">
        <div className="rating-summary">
          <div className="rating-score">{{RATING_SCORE}}</div>
          <div className="rating-stars">⭐⭐⭐⭐⭐</div>
          <p>Based on {{REVIEW_COUNT}} reviews</p>
        </div>
      </div>
    </section>
  )
}