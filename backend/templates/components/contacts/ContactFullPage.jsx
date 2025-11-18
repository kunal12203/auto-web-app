import { useState } from 'react'

export default function ContactFullPage() {
  return (
    <section className="contact-full-page">
      <div className="container">
        <div className="contact-hero">
          <h1>Let's Talk</h1>
          <p>{{CONTACT_INTRO}}</p>
        </div>
        <div className="contact-grid-full">
          <div className="contact-info-full">
            <h3>Contact Information</h3>
            <p>📧 {{CONTACT_EMAIL}}</p>
            <p>📞 {{CONTACT_PHONE}}</p>
            <p>📍 {{CONTACT_ADDRESS}}</p>
          </div>
          <form onSubmit={(e) => e.preventDefault()} className="contact-form-full">
            <input type="text" placeholder="Name" required />
            <input type="email" placeholder="Email" required />
            <textarea placeholder="Message" required />
            <button type="submit">Send</button>
          </form>
        </div>
      </div>
    </section>
  )
}