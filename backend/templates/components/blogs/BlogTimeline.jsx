export default function BlogTimeline() {
  const posts = [
    { date: '{{DATE_1}}', title: '{{TITLE_1}}', content: '{{CONTENT_1}}' },
    { date: '{{DATE_2}}', title: '{{TITLE_2}}', content: '{{CONTENT_2}}' }
  ]

  return (
    <section className="blog-timeline">
      <div className="container">
        <div className="timeline">
          {posts.map((post, i) => (
            <div key={i} className="timeline-post">
              <div className="timeline-date">{post.date}</div>
              <div className="timeline-content">
                <h3>{post.title}</h3>
                <p>{post.content}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}