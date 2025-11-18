export default function ProcessSteps() {
  const steps = [
    { number: 1, title: '{{STEP_1_TITLE}}', description: '{{STEP_1_DESC}}' },
    { number: 2, title: '{{STEP_2_TITLE}}', description: '{{STEP_2_DESC}}' },
    { number: 3, title: '{{STEP_3_TITLE}}', description: '{{STEP_3_DESC}}' },
    { number: 4, title: '{{STEP_4_TITLE}}', description: '{{STEP_4_DESC}}' }
  ]

  return (
    <section className="process-steps">
      <div className="container">
        <h2>{{PROCESS_HEADLINE}}</h2>
        <div className="steps-grid">
          {steps.map((step, i) => (
            <div key={i} className="step-item">
              <div className="step-number">{step.number}</div>
              <h3>{step.title}</h3>
              <p>{step.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}