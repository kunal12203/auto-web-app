export default function ClientLogos() {
  return (
    <section className="client-logos">
      <div className="container">
        <h3>Our Clients</h3>
        <div className="client-logos-scroll">
          <div className="logo-item">{{CLIENT_1}}</div>
          <div className="logo-item">{{CLIENT_2}}</div>
          <div className="logo-item">{{CLIENT_3}}</div>
          <div className="logo-item">{{CLIENT_4}}</div>
        </div>
      </div>
    </section>
  )
}