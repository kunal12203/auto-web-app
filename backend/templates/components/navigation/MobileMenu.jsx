import { useState } from 'react'

export default function MobileMenu() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <div className="mobile-menu">
      <button onClick={() => setIsOpen(!isOpen)} className="hamburger">
        ☰
      </button>
      {isOpen && (
        <div className="mobile-menu-overlay">
          <nav>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#contact">Contact</a>
          </nav>
        </div>
      )}
    </div>
  )
}