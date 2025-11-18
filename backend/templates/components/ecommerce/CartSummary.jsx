import { useState } from 'react'

export default function CartSummary() {
  const [items] = useState([
    { name: '{{CART_ITEM_1}}', price: '{{CART_PRICE_1}}', quantity: 1 },
    { name: '{{CART_ITEM_2}}', price: '{{CART_PRICE_2}}', quantity: 2 }
  ])

  const total = items.reduce((sum, item) => sum + (parseFloat(item.price) * item.quantity), 0)

  return (
    <section className="cart-summary">
      <div className="container">
        <h2>Your Cart</h2>
        <div className="cart-items">
          {items.map((item, i) => (
            <div key={i} className="cart-item">
              <span>{item.name}</span>
              <span>Qty: {item.quantity}</span>
              <span>${item.price}</span>
            </div>
          ))}
        </div>
        <div className="cart-total">
          <strong>Total:</strong>
          <strong>${total.toFixed(2)}</strong>
        </div>
        <button className="btn-primary">Proceed to Checkout</button>
      </div>
    </section>
  )
}