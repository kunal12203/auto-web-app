import { useState } from 'react'

export default function StepDialog({ isOpen, onClose, steps = [] }) {
  const [currentStep, setCurrentStep] = useState(0)

  const nextStep = () => {
    if (currentStep < steps.length - 1) {
      setCurrentStep(currentStep + 1)
    } else {
      onClose()
    }
  }

  const prevStep = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1)
    }
  }

  if (!isOpen) return null

  return (
    <>
      <div className="dialog-overlay" onClick={onClose} />
      <div className="dialog step-dialog">
        <div className="dialog-header">
          <h2>{steps[currentStep]?.title}</h2>
          <button onClick={onClose}>×</button>
        </div>
        <div className="step-indicator">
          Step {currentStep + 1} of {steps.length}
        </div>
        <div className="dialog-content">{steps[currentStep]?.content}</div>
        <div className="dialog-actions">
          <button onClick={prevStep} disabled={currentStep === 0}>Previous</button>
          <button onClick={nextStep}>
            {currentStep === steps.length - 1 ? 'Finish' : 'Next'}
          </button>
        </div>
      </div>
    </>
  )
}