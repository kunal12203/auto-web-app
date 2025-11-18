"""
Template Generator - Batch create component templates efficiently
"""

from pathlib import Path

COMPONENTS_DIR = Path(__file__).parent / "templates" / "components"

# Team component templates
TEAM_TEMPLATES = {
    "TeamGrid": '''export default function Team() {
  const team = [
    { name: '{{TEAM_1_NAME}}', role: '{{TEAM_1_ROLE}}', image: '{{TEAM_1_ICON}}', bio: '{{TEAM_1_BIO}}' },
    { name: '{{TEAM_2_NAME}}', role: '{{TEAM_2_ROLE}}', image: '{{TEAM_2_ICON}}', bio: '{{TEAM_2_BIO}}' },
    { name: '{{TEAM_3_NAME}}', role: '{{TEAM_3_ROLE}}', image: '{{TEAM_3_ICON}}', bio: '{{TEAM_3_BIO}}' },
    { name: '{{TEAM_4_NAME}}', role: '{{TEAM_4_ROLE}}', image: '{{TEAM_4_ICON}}', bio: '{{TEAM_4_BIO}}' }
  ]

  return (
    <section className="team team-grid" id="team">
      <div className="container">
        <h2>{{TEAM_HEADLINE}}</h2>
        <p className="section-subtitle">{{TEAM_SUBHEADLINE}}</p>
        <div className="team-grid-container">
          {team.map((member, index) => (
            <div key={index} className="team-card">
              <div className="team-image">{member.image}</div>
              <h3>{member.name}</h3>
              <p className="team-role">{member.role}</p>
              <p className="team-bio">{member.bio}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "TeamMinimal": '''export default function Team() {
  const team = [
    { name: '{{TEAM_1_NAME}}', role: '{{TEAM_1_ROLE}}' },
    { name: '{{TEAM_2_NAME}}', role: '{{TEAM_2_ROLE}}' },
    { name: '{{TEAM_3_NAME}}', role: '{{TEAM_3_ROLE}}' }
  ]

  return (
    <section className="team team-minimal" id="team">
      <div className="container">
        <h2>{{TEAM_HEADLINE}}</h2>
        <div className="team-list">
          {team.map((member, index) => (
            <div key={index} className="team-item-minimal">
              <h3>{member.name}</h3>
              <p>{member.role}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "TeamWithSocial": '''export default function Team() {
  const team = [
    { name: '{{TEAM_1_NAME}}', role: '{{TEAM_1_ROLE}}', image: '{{TEAM_1_ICON}}', social: { linkedin: '#', twitter: '#' } },
    { name: '{{TEAM_2_NAME}}', role: '{{TEAM_2_ROLE}}', image: '{{TEAM_2_ICON}}', social: { linkedin: '#', twitter: '#' } },
    { name: '{{TEAM_3_NAME}}', role: '{{TEAM_3_ROLE}}', image: '{{TEAM_3_ICON}}', social: { linkedin: '#', twitter: '#' } }
  ]

  return (
    <section className="team team-with-social" id="team">
      <div className="container">
        <h2>{{TEAM_HEADLINE}}</h2>
        <div className="team-grid-container">
          {team.map((member, index) => (
            <div key={index} className="team-card-social">
              <div className="team-image">{member.image}</div>
              <h3>{member.name}</h3>
              <p className="team-role">{member.role}</p>
              <div className="team-social">
                <a href={member.social.linkedin}>LinkedIn</a>
                <a href={member.social.twitter}>Twitter</a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "TeamLarge": '''export default function Team() {
  const team = [
    { name: '{{TEAM_1_NAME}}', role: '{{TEAM_1_ROLE}}', image: '{{TEAM_1_ICON}}', bio: '{{TEAM_1_BIO}}', email: '{{TEAM_1_EMAIL}}' },
    { name: '{{TEAM_2_NAME}}', role: '{{TEAM_2_ROLE}}', image: '{{TEAM_2_ICON}}', bio: '{{TEAM_2_BIO}}', email: '{{TEAM_2_EMAIL}}' },
    { name: '{{TEAM_3_NAME}}', role: '{{TEAM_3_ROLE}}', image: '{{TEAM_3_ICON}}', bio: '{{TEAM_3_BIO}}', email: '{{TEAM_3_EMAIL}}' }
  ]

  return (
    <section className="team team-large" id="team">
      <div className="container">
        <h2>{{TEAM_HEADLINE}}</h2>
        <p className="section-subtitle">{{TEAM_SUBHEADLINE}}</p>
        <div className="team-large-grid">
          {team.map((member, index) => (
            <div key={index} className="team-large-card">
              <div className="team-large-image">{member.image}</div>
              <div className="team-large-info">
                <h3>{member.name}</h3>
                <p className="team-role">{member.role}</p>
                <p className="team-bio">{member.bio}</p>
                <a href={`mailto:${member.email}`} className="team-email">{member.email}</a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}'''
}

# Contact/Form templates
CONTACT_TEMPLATES = {
    "ContactSimple": '''import { useState } from 'react'

export default function Contact() {
  const [formData, setFormData] = useState({ name: '', email: '', message: '' })

  const handleSubmit = (e) => {
    e.preventDefault()
    console.log('Form submitted:', formData)
  }

  return (
    <section className="contact contact-simple" id="contact">
      <div className="container">
        <h2>{{CONTACT_HEADLINE}}</h2>
        <p>{{CONTACT_SUBHEADLINE}}</p>
        <form onSubmit={handleSubmit} className="contact-form">
          <input
            type="text"
            placeholder="Your Name"
            value={formData.name}
            onChange={(e) => setFormData({...formData, name: e.target.value})}
            required
          />
          <input
            type="email"
            placeholder="Your Email"
            value={formData.email}
            onChange={(e) => setFormData({...formData, email: e.target.value})}
            required
          />
          <textarea
            placeholder="Your Message"
            value={formData.message}
            onChange={(e) => setFormData({...formData, message: e.target.value})}
            required
          />
          <button type="submit" className="submit-button">{{CONTACT_BUTTON}}</button>
        </form>
      </div>
    </section>
  )
}''',

    "ContactWithInfo": '''import { useState } from 'react'

export default function Contact() {
  const [formData, setFormData] = useState({ name: '', email: '', phone: '', message: '' })

  return (
    <section className="contact contact-with-info" id="contact">
      <div className="container">
        <h2>{{CONTACT_HEADLINE}}</h2>
        <div className="contact-grid">
          <div className="contact-info">
            <h3>Get in Touch</h3>
            <p>{{CONTACT_INFO_TEXT}}</p>
            <div className="contact-details">
              <p>📧 {{CONTACT_EMAIL}}</p>
              <p>📞 {{CONTACT_PHONE}}</p>
              <p>📍 {{CONTACT_ADDRESS}}</p>
            </div>
          </div>
          <form onSubmit={(e) => e.preventDefault()} className="contact-form">
            <input type="text" placeholder="Name" required />
            <input type="email" placeholder="Email" required />
            <input type="tel" placeholder="Phone" />
            <textarea placeholder="Message" required />
            <button type="submit">{{CONTACT_BUTTON}}</button>
          </form>
        </div>
      </div>
    </section>
  )
}'''
}

# Newsletter templates
NEWSLETTER_TEMPLATES = {
    "NewsletterSimple": '''import { useState } from 'react'

export default function Newsletter() {
  const [email, setEmail] = useState('')

  return (
    <section className="newsletter newsletter-simple">
      <div className="container">
        <h2>{{NEWSLETTER_HEADLINE}}</h2>
        <p>{{NEWSLETTER_SUBHEADLINE}}</p>
        <form onSubmit={(e) => e.preventDefault()} className="newsletter-form">
          <input
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <button type="submit">{{NEWSLETTER_BUTTON}}</button>
        </form>
      </div>
    </section>
  )
}''',

    "NewsletterInline": '''import { useState } from 'react'

export default function Newsletter() {
  return (
    <section className="newsletter newsletter-inline">
      <div className="container">
        <div className="newsletter-inline-content">
          <div className="newsletter-text">
            <h3>{{NEWSLETTER_HEADLINE}}</h3>
            <p>{{NEWSLETTER_SUBHEADLINE}}</p>
          </div>
          <form onSubmit={(e) => e.preventDefault()} className="newsletter-form-inline">
            <input type="email" placeholder="Your email" required />
            <button type="submit">{{NEWSLETTER_BUTTON}}</button>
          </form>
        </div>
      </div>
    </section>
  )
}''',

    "NewsletterBoxed": '''import { useState } from 'react'

export default function Newsletter() {
  return (
    <section className="newsletter newsletter-boxed">
      <div className="container">
        <div className="newsletter-box">
          <div className="newsletter-icon">{{NEWSLETTER_ICON}}</div>
          <h2>{{NEWSLETTER_HEADLINE}}</h2>
          <p>{{NEWSLETTER_SUBHEADLINE}}</p>
          <form onSubmit={(e) => e.preventDefault()} className="newsletter-form">
            <input type="email" placeholder="Enter your email" required />
            <button type="submit">{{NEWSLETTER_BUTTON}}</button>
          </form>
        </div>
      </div>
    </section>
  )
}'''
}

# Gallery templates
GALLERY_TEMPLATES = {
    "GalleryGrid": '''export default function Gallery() {
  const images = [
    { title: '{{GALLERY_1_TITLE}}', image: '{{GALLERY_1_ICON}}' },
    { title: '{{GALLERY_2_TITLE}}', image: '{{GALLERY_2_ICON}}' },
    { title: '{{GALLERY_3_TITLE}}', image: '{{GALLERY_3_ICON}}' },
    { title: '{{GALLERY_4_TITLE}}', image: '{{GALLERY_4_ICON}}' },
    { title: '{{GALLERY_5_TITLE}}', image: '{{GALLERY_5_ICON}}' },
    { title: '{{GALLERY_6_TITLE}}', image: '{{GALLERY_6_ICON}}' }
  ]

  return (
    <section className="gallery gallery-grid" id="gallery">
      <div className="container">
        <h2>{{GALLERY_HEADLINE}}</h2>
        <div className="gallery-grid-container">
          {images.map((item, index) => (
            <div key={index} className="gallery-item">
              <div className="gallery-image">{item.image}</div>
              <h3>{item.title}</h3>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}''',

    "GalleryMasonry": '''export default function Gallery() {
  const images = [
    { image: '{{GALLERY_1_ICON}}', category: '{{GALLERY_1_CATEGORY}}' },
    { image: '{{GALLERY_2_ICON}}', category: '{{GALLERY_2_CATEGORY}}' },
    { image: '{{GALLERY_3_ICON}}', category: '{{GALLERY_3_CATEGORY}}' },
    { image: '{{GALLERY_4_ICON}}', category: '{{GALLERY_4_CATEGORY}}' }
  ]

  return (
    <section className="gallery gallery-masonry" id="gallery">
      <div className="container">
        <h2>{{GALLERY_HEADLINE}}</h2>
        <div className="gallery-masonry-container">
          {images.map((item, index) => (
            <div key={index} className="gallery-masonry-item">
              <div className="gallery-image">{item.image}</div>
              <span className="gallery-category">{item.category}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}'''
}

# Blog templates
BLOG_TEMPLATES = {
    "BlogGrid": '''export default function Blog() {
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
}''',

    "BlogList": '''export default function Blog() {
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
}'''
}

def generate_all_templates():
    """Generate all template files"""

    categories = {
        'teams': TEAM_TEMPLATES,
        'contacts': CONTACT_TEMPLATES,
        'newsletters': NEWSLETTER_TEMPLATES,
        'galleries': GALLERY_TEMPLATES,
        'blogs': BLOG_TEMPLATES
    }

    for category, templates in categories.items():
        category_dir = COMPONENTS_DIR / category
        category_dir.mkdir(parents=True, exist_ok=True)

        for name, content in templates.items():
            file_path = category_dir / f"{name}.jsx"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Created {category}/{name}.jsx")

    print(f"\n✅ Generated {sum(len(t) for t in categories.values())} template files!")

if __name__ == "__main__":
    generate_all_templates()
