export default function SocialFollow() {
  return (
    <section className="social-follow">
      <div className="container">
        <h2>Follow Us</h2>
        <div className="social-buttons">
          <a href="{{FACEBOOK_URL}}" className="social-button facebook">Facebook</a>
          <a href="{{TWITTER_URL}}" className="social-button twitter">Twitter</a>
          <a href="{{INSTAGRAM_URL}}" className="social-button instagram">Instagram</a>
        </div>
      </div>
    </section>
  )
}