import { useState } from 'react'

export default function ApplicationForm() {
  return (
    <section className="application-form">
      <div className="container">
        <h2>Application Form</h2>
        <form onSubmit={(e) => e.preventDefault()}>
          <div className="form-section">
            <h3>Personal Information</h3>
            <input type="text" placeholder="Full Name" required />
            <input type="email" placeholder="Email" required />
            <input type="tel" placeholder="Phone" />
          </div>
          <div className="form-section">
            <h3>Experience</h3>
            <textarea placeholder="Tell us about your experience" />
            <input type="file" />
          </div>
          <button type="submit" className="btn-primary">Submit Application</button>
        </form>
      </div>
    </section>
  )
}