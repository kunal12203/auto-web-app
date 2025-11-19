export default function Footer() {
  return (
    <footer className="footer footer-centered">
      <div className="container">
        <div className="footer-centered-content">
          <div className="logo">{{BRAND_NAME}}</div>
          <nav className="footer-nav">
            <a href="#">Home</a>
            <a href="#">About</a>
            <a href="#">Services</a>
            <a href="#">Contact</a>
          </nav>
          <div className="footer-social">
            <a href="#">Facebook</a>
            <a href="#">Twitter</a>
            <a href="#">Instagram</a>
          </div>
          <p>&copy; 2024 {{BRAND_NAME}}. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}