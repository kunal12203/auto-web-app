import { useState } from 'react'

export default function ModalWithForm() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <>
      <button onClick={() => setIsOpen(true)} className="cta-button">
        Get Started
      </button>
      {isOpen && (
        <div className="modal-overlay" onClick={() => setIsOpen(false)}>
          <div className="modal-content modal-form" onClick={(e) => e.stopPropagation()}>
            <button className="modal-close" onClick={() => setIsOpen(false)}>×</button>
            <h2>Sign Up</h2>
            <form onSubmit={(e) => e.preventDefault()}>
              <input type="email" placeholder="Email" required />
              <input type="password" placeholder="Password" required />
              <button type="submit" className="btn-primary">Create Account</button>
            </form>
          </div>
        </div>
      )}
    </>
  )
}