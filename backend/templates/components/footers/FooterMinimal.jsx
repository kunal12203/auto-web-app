export default function Footer() {
  return (
    <footer className="footer footer-minimal" id="contact">
      <div className="container">
        <div className="footer-content">
          <div className="footer-brand">
            <h4>{{BRAND_NAME}}</h4>
            <p>{{BRAND_TAGLINE}}</p>
          </div>
          <div className="footer-links">
            <a href="#" aria-label="Email">Email</a>
            <a href="#" aria-label="LinkedIn">LinkedIn</a>
            <a href="#" aria-label="GitHub">GitHub</a>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2024 {{BRAND_NAME}}. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}
