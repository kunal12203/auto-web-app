export default function FAQ() {
  const faqs = [
    { question: '{{FAQ_1_QUESTION}}', answer: '{{FAQ_1_ANSWER}}' },
    { question: '{{FAQ_2_QUESTION}}', answer: '{{FAQ_2_ANSWER}}' },
    { question: '{{FAQ_3_QUESTION}}', answer: '{{FAQ_3_ANSWER}}' },
    { question: '{{FAQ_4_QUESTION}}', answer: '{{FAQ_4_ANSWER}}' }
  ]

  return (
    <section className="faq faq-simple" id="faq">
      <div className="container">
        <h2>{{FAQ_HEADLINE}}</h2>
        <div className="faq-list">
          {faqs.map((faq, index) => (
            <div key={index} className="faq-item">
              <h3>{faq.question}</h3>
              <p>{faq.answer}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
