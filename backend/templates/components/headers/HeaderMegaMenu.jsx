import { useState } from 'react'

export default function Header() {
  const [megaMenuOpen, setMegaMenuOpen] = useState(false)

  return (
    <header className="header header-mega-menu">
      <div className="container">
        <div className="logo">{{BRAND_NAME}}</div>
        <nav>
          <a href="#home">Home</a>
          <a
            href="#products"
            onMouseEnter={() => setMegaMenuOpen(true)}
            onMouseLeave={() => setMegaMenuOpen(false)}
          >
            Products
          </a>
          <a href="#pricing">Pricing</a>
          <a href="#contact">Contact</a>
        </nav>
        {megaMenuOpen && (
          <div
            className="mega-menu"
            onMouseEnter={() => setMegaMenuOpen(true)}
            onMouseLeave={() => setMegaMenuOpen(false)}
          >
            <div className="mega-menu-content">
              <div className="mega-menu-column">
                <h4>Category 1</h4>
                <a href="#">Product A</a>
                <a href="#">Product B</a>
              </div>
              <div className="mega-menu-column">
                <h4>Category 2</h4>
                <a href="#">Product C</a>
                <a href="#">Product D</a>
              </div>
            </div>
          </div>
        )}
        <button className="cta-button">Get Started</button>
      </div>
    </header>
  )
}