import { useState } from 'react'

export default function ContactFormInline() {
  return (
    <section className="contact-form-inline">
      <div className="container">
        <form onSubmit={(e) => e.preventDefault()} className="inline-form">
          <input type="text" placeholder="Name" required />
          <input type="email" placeholder="Email" required />
          <textarea placeholder="Message" required />
          <button type="submit">Send</button>
        </form>
      </div>
    </section>
  )
}