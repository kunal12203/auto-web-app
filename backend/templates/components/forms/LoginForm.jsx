import { useState } from 'react'

export default function LoginForm() {
  const [formData, setFormData] = useState({ email: '', password: '' })

  return (
    <section className="login-form">
      <div className="container">
        <div className="form-box">
          <h2>Welcome Back</h2>
          <form onSubmit={(e) => e.preventDefault()}>
            <input type="email" placeholder="Email" required />
            <input type="password" placeholder="Password" required />
            <button type="submit" className="btn-primary">Sign In</button>
            <a href="#" className="forgot-password">Forgot Password?</a>
          </form>
        </div>
      </div>
    </section>
  )
}