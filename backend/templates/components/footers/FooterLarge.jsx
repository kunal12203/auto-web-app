export default function Footer() {
  return (
    <footer className="footer footer-large">
      <div className="container">
        <div className="footer-large-grid">
          <div className="footer-col-large">
            <h4>{{BRAND_NAME}}</h4>
            <p>{{BRAND_TAGLINE}}</p>
            <div className="footer-social-large">
              <a href="#">Facebook</a>
              <a href="#">Twitter</a>
              <a href="#">Instagram</a>
              <a href="#">LinkedIn</a>
            </div>
          </div>
          <div className="footer-col">
            <h4>Products</h4>
            <a href="#">Product 1</a>
            <a href="#">Product 2</a>
            <a href="#">Product 3</a>
          </div>
          <div className="footer-col">
            <h4>Company</h4>
            <a href="#">About Us</a>
            <a href="#">Careers</a>
            <a href="#">Blog</a>
          </div>
          <div className="footer-col">
            <h4>Support</h4>
            <a href="#">Help Center</a>
            <a href="#">Contact</a>
            <a href="#">FAQ</a>
          </div>
          <div className="footer-col">
            <h4>Legal</h4>
            <a href="#">Privacy Policy</a>
            <a href="#">Terms of Service</a>
            <a href="#">Cookie Policy</a>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2024 {{BRAND_NAME}}. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}