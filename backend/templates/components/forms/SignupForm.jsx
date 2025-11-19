import { useState } from 'react'

export default function SignupForm() {
  return (
    <section className="signup-form">
      <div className="container">
        <div className="form-box">
          <h2>Create Account</h2>
          <form onSubmit={(e) => e.preventDefault()}>
            <input type="text" placeholder="Full Name" required />
            <input type="email" placeholder="Email" required />
            <input type="password" placeholder="Password" required />
            <input type="password" placeholder="Confirm Password" required />
            <button type="submit" className="btn-primary">Sign Up</button>
          </form>
        </div>
      </div>
    </section>
  )
}