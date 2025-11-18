export default function Breadcrumbs() {
  const path = [
    { label: 'Home', url: '/' },
    { label: '{{CATEGORY}}', url: '#' },
    { label: '{{PAGE}}', url: '#' }
  ]

  return (
    <nav className="breadcrumbs">
      <div className="container">
        {path.map((item, i) => (
          <span key={i}>
            <a href={item.url}>{item.label}</a>
            {i < path.length - 1 && <span> / </span>}
          </span>
        ))}
      </div>
    </nav>
  )
}