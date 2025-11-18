export default function SocialLinks() {
  const socials = [
    { name: 'Facebook', url: '{{FACEBOOK_URL}}' },
    { name: 'Twitter', url: '{{TWITTER_URL}}' },
    { name: 'Instagram', url: '{{INSTAGRAM_URL}}' },
    { name: 'LinkedIn', url: '{{LINKEDIN_URL}}' }
  ]

  return (
    <div className="social-links">
      {socials.map((social, i) => (
        <a key={i} href={social.url} className="social-link">
          {social.name}
        </a>
      ))}
    </div>
  )
}