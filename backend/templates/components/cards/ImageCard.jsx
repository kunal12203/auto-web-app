export default function ImageCard() {
  return (
    <div className="image-card">
      <div className="image-card-img">{{IMAGE}}</div>
      <div className="image-card-content">
        <h4>{{TITLE}}</h4>
        <p>{{DESCRIPTION}}</p>
      </div>
    </div>
  )
}