export default function GalleryPortfolio() {
  const projects = [
    { title: '{{PROJECT_1}}', category: '{{CATEGORY_1}}', image: '{{IMAGE_1}}' },
    { title: '{{PROJECT_2}}', category: '{{CATEGORY_2}}', image: '{{IMAGE_2}}' },
    { title: '{{PROJECT_3}}', category: '{{CATEGORY_3}}', image: '{{IMAGE_3}}' }
  ]

  return (
    <section className="gallery-portfolio">
      <div className="container">
        <h2>Portfolio</h2>
        <div className="portfolio-grid">
          {projects.map((project, i) => (
            <div key={i} className="portfolio-item">
              <div className="portfolio-image">{project.image}</div>
              <h3>{project.title}</h3>
              <span>{project.category}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}