import { useState, useEffect } from 'react'

export default function Header() {
  const [isSticky, setIsSticky] = useState(false)

  useEffect(() => {
    const handleScroll = () => {
      setIsSticky(window.scrollY > 100)
    }
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  return (
    <header className={`header header-sticky ${isSticky ? 'sticky' : ''}`}>
      <div className="container">
        <div className="logo">{{BRAND_NAME}}</div>
        <nav>
          <a href="#home">Home</a>
          <a href="#services">Services</a>
          <a href="#about">About</a>
          <a href="#contact">Contact</a>
        </nav>
        <button className="cta-button">Get Started</button>
      </div>
    </header>
  )
}