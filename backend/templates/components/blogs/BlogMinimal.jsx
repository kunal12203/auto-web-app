export default function BlogMinimal() {
  const posts = [
    { title: '{{POST_1_TITLE}}', date: '{{POST_1_DATE}}' },
    { title: '{{POST_2_TITLE}}', date: '{{POST_2_DATE}}' }
  ]

  return (
    <section className="blog-minimal">
      <div className="container">
        <ul className="blog-list-minimal">
          {posts.map((post, i) => (
            <li key={i}>
              <span className="date">{post.date}</span>
              <a href="#">{post.title}</a>
            </li>
          ))}
        </ul>
      </div>
    </section>
  )
}