import { useState } from 'react'

export default function FAQ() {
  const [openIndex, setOpenIndex] = useState(0)

  const faqs = [
    { question: '{{FAQ_1_QUESTION}}', answer: '{{FAQ_1_ANSWER}}' },
    { question: '{{FAQ_2_QUESTION}}', answer: '{{FAQ_2_ANSWER}}' },
    { question: '{{FAQ_3_QUESTION}}', answer: '{{FAQ_3_ANSWER}}' },
    { question: '{{FAQ_4_QUESTION}}', answer: '{{FAQ_4_ANSWER}}' }
  ]

  return (
    <section className="faq faq-with-cta" id="faq">
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
              </button>
              {openIndex === index && (
                <div className="faq-answer">{faq.answer}</div>
              )}
            </div>
          ))}
        </div>
        <div className="faq-cta">
          <p>{{FAQ_CTA_TEXT}}</p>
          <button className="cta-button">{{FAQ_CTA_BUTTON}}</button>
        </div>
      </div>
    </section>
  )
}
