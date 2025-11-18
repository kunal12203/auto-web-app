import { useState } from 'react'

export default function SearchBar() {
  const [query, setQuery] = useState('')

  return (
    <div className="search-bar">
      <input
        type="search"
        placeholder="Search..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button type="submit">🔍</button>
    </div>
  )
}