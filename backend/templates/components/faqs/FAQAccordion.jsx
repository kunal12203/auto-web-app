import { useState } from 'react'

export default function FAQ() {
  const [openIndex, setOpenIndex] = useState(null)

  const faqs = [
    { question: '{{FAQ_1_QUESTION}}', answer: '{{FAQ_1_ANSWER}}' },
    { question: '{{FAQ_2_QUESTION}}', answer: '{{FAQ_2_ANSWER}}' },
    { question: '{{FAQ_3_QUESTION}}', answer: '{{FAQ_3_ANSWER}}' },
    { question: '{{FAQ_4_QUESTION}}', answer: '{{FAQ_4_ANSWER}}' },
    { question: '{{FAQ_5_QUESTION}}', answer: '{{FAQ_5_ANSWER}}' }
  ]

  return (
    <section className="faq faq-accordion" id="faq">
      <div className="container">
        <h2>{{FAQ_HEADLINE}}</h2>
        <p className="section-subtitle">{{FAQ_SUBHEADLINE}}</p>
        <div className="faq-list">
          {faqs.map((faq, index) => (
            <div key={index} className="faq-item">
              <button
                className={`faq-question ${openIndex === index ? 'active' : ''}`}
                onClick={() => setOpenIndex(openIndex === index ? null : index)}
              >
                {faq.question}
                <span className="faq-icon">{openIndex === index ? '−' : '+'}</span>
              </button>
              {openIndex === index && (
                <div className="faq-answer">{faq.answer}</div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
