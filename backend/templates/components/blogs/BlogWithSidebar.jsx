export default function BlogWithSidebar() {
  const posts = [
    { title: '{{POST_1_TITLE}}', excerpt: '{{POST_1_EXCERPT}}' },
    { title: '{{POST_2_TITLE}}', excerpt: '{{POST_2_EXCERPT}}' }
  ]

  return (
    <section className="blog-with-sidebar">
      <div className="container">
        <div className="blog-layout">
          <div className="blog-main">
            {posts.map((post, i) => (
              <article key={i} className="blog-post">
                <h3>{post.title}</h3>
                <p>{post.excerpt}</p>
              </article>
            ))}
          </div>
          <aside className="blog-sidebar">
            <h4>Recent Posts</h4>
            <ul>
              <li><a href="#">Post 1</a></li>
              <li><a href="#">Post 2</a></li>
            </ul>
          </aside>
        </div>
      </div>
    </section>
  )
}