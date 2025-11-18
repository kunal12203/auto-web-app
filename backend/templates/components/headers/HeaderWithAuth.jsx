import { useState } from 'react'

export default function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  return (
    <header className="header header-with-auth">
      <div className="container">
        <div className="logo">{{BRAND_NAME}}</div>
        <nav className={isMenuOpen ? 'nav-open' : ''}>
          <a href="#features">Features</a>
          <a href="#pricing">Pricing</a>
          <a href="#about">About</a>
        </nav>
        <div className="header-auth">
          <button className="btn-ghost">Sign In</button>
          <button className="cta-button">Sign Up</button>
        </div>
        <button
          className="menu-toggle"
          onClick={() => setIsMenuOpen(!isMenuOpen)}
        >
          ☰
        </button>
      </div>
    </header>
  )
}