export default function ReadingTime({ minutes = 5 }) {
  return (
    <div className="reading-time">
      📖 {minutes} min read
    </div>
  )
}