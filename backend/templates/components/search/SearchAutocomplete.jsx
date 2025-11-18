import { useState } from 'react'

export default function SearchAutocomplete() {
  const [query, setQuery] = useState('')
  const [showSuggestions, setShowSuggestions] = useState(false)

  const suggestions = ['{{SUGGESTION_1}}', '{{SUGGESTION_2}}', '{{SUGGESTION_3}}']

  return (
    <div className="search-autocomplete">
      <input
        type="search"
        placeholder="Type to search..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onFocus={() => setShowSuggestions(true)}
        onBlur={() => setTimeout(() => setShowSuggestions(false), 200)}
      />
      {showSuggestions && query && (
        <div className="suggestions">
          {suggestions.filter(s => s.toLowerCase().includes(query.toLowerCase())).map((s, i) => (
            <div key={i} className="suggestion-item">{s}</div>
          ))}
        </div>
      )}
    </div>
  )
}