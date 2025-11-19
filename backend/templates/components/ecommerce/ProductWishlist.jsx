import { useState } from 'react'

export default function ProductWishlist() {
  const [wishlist, setWishlist] = useState([
    { name: '{{PRODUCT_1}}', price: '{{PRICE_1}}' }
  ])

  return (
    <section className="product-wishlist">
      <div className="container">
        <h2>My Wishlist</h2>
        <div className="wishlist-items">
          {wishlist.map((item, i) => (
            <div key={i} className="wishlist-item">
              <h3>{item.name}</h3>
              <p>${item.price}</p>
              <button>Add to Cart</button>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}