export default function ProductGrid() {
  const products = [
    { name: '{{PRODUCT_1_NAME}}', price: '{{PRODUCT_1_PRICE}}', image: '{{PRODUCT_1_ICON}}', rating: '{{PRODUCT_1_RATING}}' },
    { name: '{{PRODUCT_2_NAME}}', price: '{{PRODUCT_2_PRICE}}', image: '{{PRODUCT_2_ICON}}', rating: '{{PRODUCT_2_RATING}}' },
    { name: '{{PRODUCT_3_NAME}}', price: '{{PRODUCT_3_PRICE}}', image: '{{PRODUCT_3_ICON}}', rating: '{{PRODUCT_3_RATING}}' },
    { name: '{{PRODUCT_4_NAME}}', price: '{{PRODUCT_4_PRICE}}', image: '{{PRODUCT_4_ICON}}', rating: '{{PRODUCT_4_RATING}}' }
  ]

  return (
    <section className="products product-grid">
      <div className="container">
        <h2>{{PRODUCTS_HEADLINE}}</h2>
        <div className="product-grid-container">
          {products.map((product, i) => (
            <div key={i} className="product-card">
              <div className="product-image">{product.image}</div>
              <h3>{product.name}</h3>
              <div className="product-rating">⭐ {product.rating}</div>
              <div className="product-price">${product.price}</div>
              <button className="add-to-cart">Add to Cart</button>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}