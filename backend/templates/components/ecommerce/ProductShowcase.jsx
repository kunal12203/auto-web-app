export default function ProductShowcase() {
  return (
    <section className="product-showcase">
      <div className="container">
        <div className="showcase-grid">
          <div className="showcase-image">
            <div className="product-image-large">{{PRODUCT_ICON}}</div>
          </div>
          <div className="showcase-info">
            <h2>{{PRODUCT_NAME}}</h2>
            <div className="product-rating">⭐⭐⭐⭐⭐ ({{PRODUCT_REVIEWS}} reviews)</div>
            <div className="product-price-large">${{PRODUCT_PRICE}}</div>
            <p>{{PRODUCT_DESCRIPTION}}</p>
            <div className="product-features">
              <ul>
                <li>{{FEATURE_1}}</li>
                <li>{{FEATURE_2}}</li>
                <li>{{FEATURE_3}}</li>
              </ul>
            </div>
            <button className="btn-primary">Buy Now</button>
          </div>
        </div>
      </div>
    </section>
  )
}