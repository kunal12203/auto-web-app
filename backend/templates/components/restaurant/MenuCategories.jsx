import { useState } from 'react'

export default function MenuCategories() {
  const [category, setCategory] = useState('all')

  return (
    <section className="menu-categories">
      <div className="container">
        <div className="menu-tabs">
          <button onClick={() => setCategory('all')}>All</button>
          <button onClick={() => setCategory('appetizers')}>Appetizers</button>
          <button onClick={() => setCategory('mains')}>Mains</button>
          <button onClick={() => setCategory('desserts')}>Desserts</button>
        </div>
        <div className="menu-items">
          <p>Menu items for {category}</p>
        </div>
      </div>
    </section>
  )
}