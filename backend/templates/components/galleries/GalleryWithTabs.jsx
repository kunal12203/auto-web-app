import { useState } from 'react'

export default function GalleryWithTabs() {
  const [category, setCategory] = useState('all')

  return (
    <section className="gallery-with-tabs">
      <div className="container">
        <h2>{{GALLERY_HEADLINE}}</h2>
        <div className="gallery-tabs">
          <button onClick={() => setCategory('all')}>All</button>
          <button onClick={() => setCategory('recent')}>Recent</button>
          <button onClick={() => setCategory('popular')}>Popular</button>
        </div>
        <div className="gallery-grid">
          <div className="gallery-item">{{GALLERY_ITEM}}</div>
        </div>
      </div>
    </section>
  )
}