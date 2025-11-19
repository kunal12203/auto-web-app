export default function SpecialOffers() {
  const offers = [
    { title: '{{OFFER_1_TITLE}}', description: '{{OFFER_1_DESC}}', discount: '{{OFFER_1_DISCOUNT}}' },
    { title: '{{OFFER_2_TITLE}}', description: '{{OFFER_2_DESC}}', discount: '{{OFFER_2_DISCOUNT}}' }
  ]

  return (
    <section className="special-offers">
      <div className="container">
        <h2>Special Offers</h2>
        <div className="offers-grid">
          {offers.map((offer, i) => (
            <div key={i} className="offer-card">
              <span className="offer-badge">{offer.discount} OFF</span>
              <h3>{offer.title}</h3>
              <p>{offer.description}</p>
              <button>Claim Offer</button>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}