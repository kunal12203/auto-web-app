import { useState } from 'react'

export default function TabNavigation() {
  const [active, setActive] = useState('overview')

  return (
    <nav className="tab-navigation">
      <button
        className={active === 'overview' ? 'active' : ''}
        onClick={() => setActive('overview')}
      >
        Overview
      </button>
      <button
        className={active === 'specs' ? 'active' : ''}
        onClick={() => setActive('specs')}
      >
        Specifications
      </button>
      <button
        className={active === 'reviews' ? 'active' : ''}
        onClick={() => setActive('reviews')}
      >
        Reviews
      </button>
    </nav>
  )
}