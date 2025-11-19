export default function MenuSection() {
  const menuItems = [
    { name: '{{MENU_ITEM_1}}', description: '{{MENU_DESC_1}}', price: '{{MENU_PRICE_1}}' },
    { name: '{{MENU_ITEM_2}}', description: '{{MENU_DESC_2}}', price: '{{MENU_PRICE_2}}' },
    { name: '{{MENU_ITEM_3}}', description: '{{MENU_DESC_3}}', price: '{{MENU_PRICE_3}}' },
    { name: '{{MENU_ITEM_4}}', description: '{{MENU_DESC_4}}', price: '{{MENU_PRICE_4}}' }
  ]

  return (
    <section className="menu-section">
      <div className="container">
        <h2>{{MENU_HEADLINE}}</h2>
        <div className="menu-grid">
          {menuItems.map((item, i) => (
            <div key={i} className="menu-item">
              <div className="menu-item-header">
                <h3>{item.name}</h3>
                <span className="menu-price">${item.price}</span>
              </div>
              <p>{item.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}