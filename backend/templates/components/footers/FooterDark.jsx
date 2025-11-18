export default function Footer() {
  return (
    <footer className="footer footer-dark">
      <div className="container">
        <div className="footer-grid">
          <div className="footer-col">
            <h4>{{BRAND_NAME}}</h4>
            <p>{{BRAND_TAGLINE}}</p>
          </div>
          <div className="footer-col">
            <h4>Company</h4>
            <a href="#">About</a>
            <a href="#">Team</a>
            <a href="#">Careers</a>
          </div>
          <div className="footer-col">
            <h4>Resources</h4>
            <a href="#">Blog</a>
            <a href="#">Help Center</a>
            <a href="#">Contact</a>
          </div>
          <div className="footer-col">
            <h4>Connect</h4>
            <a href="#">Facebook</a>
            <a href="#">Twitter</a>
            <a href="#">LinkedIn</a>
          </div>
        </div>
        <div className="footer-bottom-dark">
          <p>&copy; 2024 {{BRAND_NAME}}. All rights reserved.</p>
          <div className="footer-legal">
            <a href="#">Privacy Policy</a>
            <a href="#">Terms of Service</a>
          </div>
        </div>
      </div>
    </footer>
  )
}