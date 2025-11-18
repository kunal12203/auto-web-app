export default function Footer() {
  return (
    <footer className="footer footer-with-map">
      <div className="container">
        <div className="footer-map-grid">
          <div className="footer-info">
            <h4>{{BRAND_NAME}}</h4>
            <p>📍 {{CONTACT_ADDRESS}}</p>
            <p>📞 {{CONTACT_PHONE}}</p>
            <p>📧 {{CONTACT_EMAIL}}</p>
          </div>
          <div className="footer-map">
            <div className="map-placeholder">🗺️ Map</div>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2024 {{BRAND_NAME}}. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}