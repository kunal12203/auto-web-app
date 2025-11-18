export default function Header() {
  return (
    <header className="header header-centered">
      <div className="container">
        <div className="header-centered-content">
          <div className="logo">{{BRAND_NAME}}</div>
          <nav>
            <a href="#home">Home</a>
            <a href="#work">Work</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
          </nav>
        </div>
      </div>
    </header>
  )
}