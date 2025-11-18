export default function ProfileCard() {
  return (
    <div className="profile-card">
      <div className="profile-avatar">{{AVATAR}}</div>
      <h3>{{NAME}}</h3>
      <p className="profile-title">{{TITLE}}</p>
      <p className="profile-bio">{{BIO}}</p>
    </div>
  )
}