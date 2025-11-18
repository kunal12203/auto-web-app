export default function ProductRatingStars({ rating = 4 }) {
  return (
    <div className="rating-stars">
      {[1,2,3,4,5].map(star => (
        <span key={star} className={star <= rating ? 'star-filled' : 'star-empty'}>
          ⭐
        </span>
      ))}
    </div>
  )
}