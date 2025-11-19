import { useState } from 'react'

export default function QuoteForm() {
  return (
    <section className="quote-form">
      <div className="container">
        <h2>Get a Free Quote</h2>
        <form onSubmit={(e) => e.preventDefault()}>
          <div className="form-row">
            <input type="text" placeholder="Your Name" required />
            <input type="email" placeholder="Email" required />
          </div>
          <div className="form-row">
            <input type="tel" placeholder="Phone" />
            <select>
              <option>Select Service</option>
              <option>Service A</option>
              <option>Service B</option>
            </select>
          </div>
          <textarea placeholder="Project Details" required />
          <button type="submit" className="btn-primary">Request Quote</button>
        </form>
      </div>
    </section>
  )
}