export default function Footer() {
  return (
    <footer className="footer" id="contact">
      <div className="container">
        <div className="footer-grid">
          <div className="footer-col">
            <h4>{{BRAND_NAME}}</h4>
            <p>{{BRAND_TAGLINE}}</p>
          </div>
          <div className="footer-col">
            <h4>Quick Links</h4>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#contact">Contact</a>
          </div>
          <div className="footer-col">
            <h4>Contact Us</h4>
            <p>📧 {{CONTACT_EMAIL}}</p>
            <p>📞 {{CONTACT_PHONE}}</p>
            <p>📍 {{CONTACT_ADDRESS}}</p>
          </div>
          <div className="footer-col">
            <h4>Follow Us</h4>
            <div className="social-links">
              <a href="#" aria-label="Facebook">Facebook</a>
              <a href="#" aria-label="Instagram">Instagram</a>
              <a href="#" aria-label="Twitter">Twitter</a>
            </div>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2024 {{BRAND_NAME}}. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}
