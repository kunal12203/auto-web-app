import { useState } from 'react'

export default function ContactMinimal() {
  return (
    <section className="contact-minimal">
      <div className="container">
        <h2>Contact</h2>
        <p>{{CONTACT_EMAIL}}</p>
        <p>{{CONTACT_PHONE}}</p>
      </div>
    </section>
  )
}