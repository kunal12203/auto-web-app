export default function NewsCard() {
  return (
    <div className="news-card">
      <span className="news-date">{{DATE}}</span>
      <h4>{{TITLE}}</h4>
      <p>{{EXCERPT}}</p>
      <a href="#">Read More</a>
    </div>
  )
}