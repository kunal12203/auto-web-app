import { useState } from 'react'

export default function ProductCarousel() {
  const [currentIndex, setCurrentIndex] = useState(0)
  
  const products = [
    { name: '{{PRODUCT_1_NAME}}', price: '{{PRODUCT_1_PRICE}}', image: '{{PRODUCT_1_ICON}}' },
    { name: '{{PRODUCT_2_NAME}}', price: '{{PRODUCT_2_PRICE}}', image: '{{PRODUCT_2_ICON}}' },
    { name: '{{PRODUCT_3_NAME}}', price: '{{PRODUCT_3_PRICE}}', image: '{{PRODUCT_3_ICON}}' }
  ]

  return (
    <section className="product-carousel">
      <div className="container">
        <h2>{{CAROUSEL_HEADLINE}}</h2>
        <div className="carousel-container">
          <button onClick={() => setCurrentIndex(Math.max(0, currentIndex - 1))}>←</button>
          <div className="carousel-item">
            <div className="product-image">{products[currentIndex].image}</div>
            <h3>{products[currentIndex].name}</h3>
            <p>${products[currentIndex].price}</p>
          </div>
          <button onClick={() => setCurrentIndex(Math.min(products.length - 1, currentIndex + 1))}>→</button>
        </div>
      </div>
    </section>
  )
}