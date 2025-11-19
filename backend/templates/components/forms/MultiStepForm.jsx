import { useState } from 'react'

export default function MultiStepForm() {
  const [step, setStep] = useState(1)

  return (
    <section className="multi-step-form">
      <div className="container">
        <div className="progress-steps">
          <span className={step >= 1 ? 'active' : ''}>1. Info</span>
          <span className={step >= 2 ? 'active' : ''}>2. Details</span>
          <span className={step >= 3 ? 'active' : ''}>3. Confirm</span>
        </div>
        <form onSubmit={(e) => e.preventDefault()}>
          {step === 1 && (
            <div className="form-step">
              <h3>Personal Information</h3>
              <input type="text" placeholder="Name" />
              <input type="email" placeholder="Email" />
            </div>
          )}
          {step === 2 && (
            <div className="form-step">
              <h3>Additional Details</h3>
              <input type="tel" placeholder="Phone" />
              <textarea placeholder="Message" />
            </div>
          )}
          {step === 3 && (
            <div className="form-step">
              <h3>Confirmation</h3>
              <p>Please review your information</p>
            </div>
          )}
          <div className="form-actions">
            {step > 1 && <button onClick={() => setStep(step - 1)}>Back</button>}
            {step < 3 ? (
              <button onClick={() => setStep(step + 1)}>Next</button>
            ) : (
              <button type="submit">Submit</button>
            )}
          </div>
        </form>
      </div>
    </section>
  )
}