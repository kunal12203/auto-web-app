export default function BlogFeatured() {
  return (
    <section className="blog-featured">
      <div className="container">
        <div className="featured-post">
          <div className="featured-image">{{FEATURED_IMAGE}}</div>
          <div className="featured-content">
            <span className="category">{{CATEGORY}}</span>
            <h2>{{FEATURED_TITLE}}</h2>
            <p>{{FEATURED_EXCERPT}}</p>
            <a href="#" className="read-more">Read More →</a>
          </div>
        </div>
      </div>
    </section>
  )
}