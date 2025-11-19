export default function FAQ() {
  const faqs = [
    { question: '{{FAQ_1_QUESTION}}', answer: '{{FAQ_1_ANSWER}}' },
    { question: '{{FAQ_2_QUESTION}}', answer: '{{FAQ_2_ANSWER}}' },
    { question: '{{FAQ_3_QUESTION}}', answer: '{{FAQ_3_ANSWER}}' }
  ]

  return (
    <section className="faq faq-minimal" id="faq">
      <div className="container">
        <h2>{{FAQ_HEADLINE}}</h2>
        <div className="faq-list-minimal">
          {faqs.map((faq, index) => (
            <div key={index} className="faq-item-minimal">
              <dt>{faq.question}</dt>
              <dd>{faq.answer}</dd>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
