export default function IconCards() {
  const items = [
    { icon: '{{ICON_1}}', title: '{{TITLE_1}}' },
    { icon: '{{ICON_2}}', title: '{{TITLE_2}}' },
    { icon: '{{ICON_3}}', title: '{{TITLE_3}}' },
    { icon: '{{ICON_4}}', title: '{{TITLE_4}}' }
  ]

  return (
    <section className="icon-cards">
      <div className="container">
        <div className="icon-cards-grid">
          {items.map((item, i) => (
            <div key={i} className="icon-card">
              <div className="icon-large">{item.icon}</div>
              <h3>{item.title}</h3>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}