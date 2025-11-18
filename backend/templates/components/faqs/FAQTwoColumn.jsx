export default function FAQ() {
  const leftFaqs = [
    { question: '{{FAQ_1_QUESTION}}', answer: '{{FAQ_1_ANSWER}}' },
    { question: '{{FAQ_2_QUESTION}}', answer: '{{FAQ_2_ANSWER}}' },
    { question: '{{FAQ_3_QUESTION}}', answer: '{{FAQ_3_ANSWER}}' }
  ]

  const rightFaqs = [
    { question: '{{FAQ_4_QUESTION}}', answer: '{{FAQ_4_ANSWER}}' },
    { question: '{{FAQ_5_QUESTION}}', answer: '{{FAQ_5_ANSWER}}' },
    { question: '{{FAQ_6_QUESTION}}', answer: '{{FAQ_6_ANSWER}}' }
  ]

  return (
    <section className="faq faq-two-column" id="faq">
      <div className="container">
        <h2>{{FAQ_HEADLINE}}</h2>
        <p className="section-subtitle">{{FAQ_SUBHEADLINE}}</p>
        <div className="faq-grid">
          <div className="faq-column">
            {leftFaqs.map((faq, index) => (
              <div key={index} className="faq-item">
                <h3>{faq.question}</h3>
                <p>{faq.answer}</p>
              </div>
            ))}
          </div>
          <div className="faq-column">
            {rightFaqs.map((faq, index) => (
              <div key={index} className="faq-item">
                <h3>{faq.question}</h3>
                <p>{faq.answer}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}
