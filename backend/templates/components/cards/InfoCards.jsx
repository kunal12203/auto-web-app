export default function InfoCards() {
  const cards = [
    { title: '{{CARD_1_TITLE}}', description: '{{CARD_1_DESC}}', link: '{{CARD_1_LINK}}' },
    { title: '{{CARD_2_TITLE}}', description: '{{CARD_2_DESC}}', link: '{{CARD_2_LINK}}' }
  ]

  return (
    <section className="info-cards">
      <div className="container">
        <div className="info-cards-grid">
          {cards.map((card, i) => (
            <div key={i} className="info-card">
              <h3>{card.title}</h3>
              <p>{card.description}</p>
              <a href={card.link} className="card-link">Learn More →</a>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}