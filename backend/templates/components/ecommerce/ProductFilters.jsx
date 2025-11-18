import { useState } from 'react'

export default function ProductFilters() {
  const [category, setCategory] = useState('all')
  const [priceRange, setPriceRange] = useState('all')

  return (
    <section className="product-filters">
      <div className="container">
        <div className="filters-bar">
          <select value={category} onChange={(e) => setCategory(e.target.value)}>
            <option value="all">All Categories</option>
            <option value="electronics">Electronics</option>
            <option value="clothing">Clothing</option>
          </select>
          <select value={priceRange} onChange={(e) => setPriceRange(e.target.value)}>
            <option value="all">All Prices</option>
            <option value="under50">Under $50</option>
            <option value="50-100">$50-$100</option>
          </select>
        </div>
      </div>
    </section>
  )
}