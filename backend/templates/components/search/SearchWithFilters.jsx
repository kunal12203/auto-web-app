import { useState } from 'react'

export default function SearchWithFilters() {
  const [query, setQuery] = useState('')
  const [category, setCategory] = useState('all')

  return (
    <div className="search-with-filters">
      <div className="search-input">
        <input
          type="search"
          placeholder="Search..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button>Search</button>
      </div>
      <div className="search-filters">
        <select value={category} onChange={(e) => setCategory(e.target.value)}>
          <option value="all">All Categories</option>
          <option value="products">Products</option>
          <option value="services">Services</option>
        </select>
      </div>
    </div>
  )
}