import { useState } from 'react'

export default function ProductQuickView() {
  const [showQuickView, setShowQuickView] = useState(false)

  return (
    <>
      <button onClick={() => setShowQuickView(true)}>Quick View</button>
      {showQuickView && (
        <div className="quick-view-overlay" onClick={() => setShowQuickView(false)}>
          <div className="quick-view-content" onClick={(e) => e.stopPropagation()}>
            <button className="close" onClick={() => setShowQuickView(false)}>×</button>
            <div className="quick-view-grid">
              <div className="quick-view-image">{{PRODUCT_IMAGE}}</div>
              <div className="quick-view-info">
                <h3>{{PRODUCT_NAME}}</h3>
                <p className="price">${{PRODUCT_PRICE}}</p>
                <button className="add-to-cart">Add to Cart</button>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  )
}