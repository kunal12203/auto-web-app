import { useState } from 'react'

export default function ContactSplit() {
  return (
    <section className="contact-split">
      <div className="contact-split-container">
        <div className="contact-map">
          <div className="map-placeholder">🗺️ Map</div>
        </div>
        <div className="contact-form-side">
          <h2>Get in Touch</h2>
          <form onSubmit={(e) => e.preventDefault()}>
            <input type="text" placeholder="Name" required />
            <input type="email" placeholder="Email" required />
            <textarea placeholder="Message" required />
            <button type="submit">Send Message</button>
          </form>
        </div>
      </div>
    </section>
  )
}