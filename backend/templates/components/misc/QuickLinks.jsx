export default function QuickLinks() {
  const links = [
    { title: '{{LINK_1}}', url: '#' },
    { title: '{{LINK_2}}', url: '#' },
    { title: '{{LINK_3}}', url: '#' }
  ]

  return (
    <div className="quick-links">
      <h4>Quick Links</h4>
      {links.map((link, i) => (
        <a key={i} href={link.url}>{link.title}</a>
      ))}
    </div>
  )
}