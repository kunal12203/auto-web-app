import { useState } from 'react'

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
}