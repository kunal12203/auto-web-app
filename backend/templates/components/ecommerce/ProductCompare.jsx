export default function ProductCompare() {
  const products = [
    { name: '{{PRODUCT_1}}', price: '{{PRICE_1}}', rating: '{{RATING_1}}' },
    { name: '{{PRODUCT_2}}', price: '{{PRICE_2}}', rating: '{{RATING_2}}' }
  ]

  return (
    <section className="product-compare">
      <div className="container">
        <h2>Compare Products</h2>
        <table className="compare-table">
          <thead>
            <tr>
              <th>Feature</th>
              {products.map((p, i) => (
                <th key={i}>{p.name}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Price</td>
              {products.map((p, i) => (
                <td key={i}>${p.price}</td>
              ))}
            </tr>
            <tr>
              <td>Rating</td>
              {products.map((p, i) => (
                <td key={i}>{p.rating}⭐</td>
              ))}
            </tr>
          </tbody>
        </table>
      </div>
    </section>
  )
}