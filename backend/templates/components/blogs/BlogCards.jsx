export default function BlogCards() {
  const posts = [
    { title: '{{POST_1_TITLE}}', excerpt: '{{POST_1_EXCERPT}}', image: '{{IMAGE_1}}', author: '{{AUTHOR_1}}' },
    { title: '{{POST_2_TITLE}}', excerpt: '{{POST_2_EXCERPT}}', image: '{{IMAGE_2}}', author: '{{AUTHOR_2}}' }
  ]

  return (
    <section className="blog-cards">
      <div className="container">
        <div className="blog-cards-grid">
          {posts.map((post, i) => (
            <article key={i} className="blog-card-item">
              <div className="blog-card-image">{post.image}</div>
              <h3>{post.title}</h3>
              <p>{post.excerpt}</p>
              <div className="blog-meta">
                <span>By {post.author}</span>
                <a href="#">Read →</a>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  )
}