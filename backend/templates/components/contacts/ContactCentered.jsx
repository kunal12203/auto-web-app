import { useState } from 'react'

export default function ContactCentered() {
  return (
    <section className="contact-centered">
      <div className="container">
        <div className="contact-box-centered">
          <h2>Get In Touch</h2>
          <form onSubmit={(e) => e.preventDefault()}>
            <input type="email" placeholder="Your Email" required />
            <textarea placeholder="Your Message" required />
            <button type="submit" className="btn-primary">Send</button>
          </form>
        </div>
      </div>
    </section>
  )
}