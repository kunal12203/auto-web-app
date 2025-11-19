import { useState } from 'react'

export default function Header() {
  const [searchOpen, setSearchOpen] = useState(false)

  return (
    <header className="header header-with-search">
      <div className="container">
        <div className="logo">{{BRAND_NAME}}</div>
        <nav>
          <a href="#home">Home</a>
          <a href="#products">Products</a>
          <a href="#about">About</a>
          <a href="#contact">Contact</a>
        </nav>
        <div className="header-actions">
          <button onClick={() => setSearchOpen(!searchOpen)}>🔍</button>
          <button className="cta-button">Get Started</button>
        </div>
        {searchOpen && (
          <div className="search-bar">
            <input type="search" placeholder="Search..." />
          </div>
        )}
      </div>
    </header>
  )
}