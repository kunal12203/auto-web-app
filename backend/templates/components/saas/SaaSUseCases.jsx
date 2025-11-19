export default function SaaSUseCases() {
  const useCases = [
    { title: '{{USECASE_1_TITLE}}', description: '{{USECASE_1_DESC}}', icon: '{{ICON_1}}' },
    { title: '{{USECASE_2_TITLE}}', description: '{{USECASE_2_DESC}}', icon: '{{ICON_2}}' }
  ]

  return (
    <section className="saas-use-cases">
      <div className="container">
        <h2>Use Cases</h2>
        <div className="use-cases-grid">
          {useCases.map((useCase, i) => (
            <div key={i} className="use-case-card">
              <div className="use-case-icon">{useCase.icon}</div>
              <h3>{useCase.title}</h3>
              <p>{useCase.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}