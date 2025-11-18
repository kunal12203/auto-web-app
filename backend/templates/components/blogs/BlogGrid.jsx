export default function Blog() {
  const posts = [
    { title: '{{BLOG_1_TITLE}}', excerpt: '{{BLOG_1_EXCERPT}}', date: '{{BLOG_1_DATE}}', category: '{{BLOG_1_CATEGORY}}' },
    { title: '{{BLOG_2_TITLE}}', excerpt: '{{BLOG_2_EXCERPT}}', date: '{{BLOG_2_DATE}}', category: '{{BLOG_2_CATEGORY}}' },
    { title: '{{BLOG_3_TITLE}}', excerpt: '{{BLOG_3_EXCERPT}}', date: '{{BLOG_3_DATE}}', category: '{{BLOG_3_CATEGORY}}' }
  ]

  return (
    <section className="blog blog-grid" id="blog">
      <div className="container">
        <h2>{{BLOG_HEADLINE}}</h2>
        <div className="blog-grid-container">
          {posts.map((post, index) => (
            <article key={index} className="blog-card">
              <span className="blog-category">{post.category}</span>
              <h3>{post.title}</h3>
              <p>{post.excerpt}</p>
              <div className="blog-meta">
                <span className="blog-date">{post.date}</span>
                <a href="#" className="blog-read-more">Read More →</a>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  )
}