export default function StepIndicator({ currentStep = 1, totalSteps = 4 }) {
  return (
    <div className="step-indicator">
      {Array.from({ length: totalSteps }, (_, i) => i + 1).map(step => (
        <div
          key={step}
          className={`step ${step <= currentStep ? 'completed' : ''}`}
        >
          {step}
        </div>
      ))}
    </div>
  )
}