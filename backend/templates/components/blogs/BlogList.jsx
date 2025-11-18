export default function Blog() {
  const posts = [
    { title: '{{BLOG_1_TITLE}}', excerpt: '{{BLOG_1_EXCERPT}}', date: '{{BLOG_1_DATE}}', author: '{{BLOG_1_AUTHOR}}' },
    { title: '{{BLOG_2_TITLE}}', excerpt: '{{BLOG_2_EXCERPT}}', date: '{{BLOG_2_DATE}}', author: '{{BLOG_2_AUTHOR}}' },
    { title: '{{BLOG_3_TITLE}}', excerpt: '{{BLOG_3_EXCERPT}}', date: '{{BLOG_3_DATE}}', author: '{{BLOG_3_AUTHOR}}' }
  ]

  return (
    <section className="blog blog-list" id="blog">
      <div className="container">
        <h2>{{BLOG_HEADLINE}}</h2>
        <div className="blog-list-container">
          {posts.map((post, index) => (
            <article key={index} className="blog-list-item">
              <div className="blog-list-date">{post.date}</div>
              <div className="blog-list-content">
                <h3>{post.title}</h3>
                <p>{post.excerpt}</p>
                <div className="blog-list-meta">
                  <span>By {post.author}</span>
                  <a href="#">Read More →</a>
                </div>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  )
}