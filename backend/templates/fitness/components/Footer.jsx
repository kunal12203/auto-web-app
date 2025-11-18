export default function Footer() {
  return (
    <footer className="footer" id="contact">
      <div className="container">
        <div className="footer-grid">
          <div className="footer-col">
            <h4>FitLife Gym</h4>
            <p>Your partner in achieving the ultimate fitness transformation</p>
          </div>
          <div className="footer-col">
            <h4>Quick Links</h4>
            <a href="#home">Home</a>
            <a href="#services">Services</a>
            <a href="#pricing">Pricing</a>
            <a href="#testimonials">Testimonials</a>
          </div>
          <div className="footer-col">
            <h4>Contact Us</h4>
            <p>📧 info@fitlifegym.com</p>
            <p>📞 (555) 123-4567</p>
            <p>📍 123 Fitness Street, Healthy City, HC 12345</p>
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
          <p>&copy; 2024 FitLife Gym. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}
