import { useState } from 'react'
import './PaymentGatewaySelector.css'

function PaymentGatewaySelector({ question, options, onSelect }) {
  const [selected, setSelected] = useState(options[0])

  const gatewayInfo = {
    stripe: {
      name: 'Stripe',
      description: 'Popular payment gateway with excellent documentation',
      icon: '💳',
      features: ['Credit cards', 'ACH', 'Apple Pay', 'Google Pay']
    },
    paypal: {
      name: 'PayPal',
      description: 'Widely used payment platform worldwide',
      icon: '🅿️',
      features: ['PayPal balance', 'Credit cards', 'Bank transfers']
    },
    razorpay: {
      name: 'Razorpay',
      description: 'Popular payment gateway in India',
      icon: '💰',
      features: ['UPI', 'Cards', 'Net banking', 'Wallets']
    },
    none: {
      name: 'Skip Payment',
      description: 'Continue without payment integration',
      icon: '⏭️',
      features: ['Add payment later']
    }
  }

  const handleSelect = () => {
    onSelect(selected)
  }

  return (
    <div className="payment-gateway-modal">
      <div className="payment-gateway-overlay" />
      <div className="payment-gateway-content">
        <div className="payment-gateway-header">
          <h2>{question}</h2>
          <p>Choose a payment gateway to integrate into your project</p>
        </div>

        <div className="gateway-options">
          {options.map(option => {
            const info = gatewayInfo[option]
            if (!info) return null

            return (
              <div
                key={option}
                className={`gateway-option ${selected === option ? 'selected' : ''}`}
                onClick={() => setSelected(option)}
              >
                <div className="gateway-icon">{info.icon}</div>
                <div className="gateway-details">
                  <h3>{info.name}</h3>
                  <p>{info.description}</p>
                  <div className="gateway-features">
                    {info.features.map((feature, i) => (
                      <span key={i} className="feature-tag">{feature}</span>
                    ))}
                  </div>
                </div>
                <div className="gateway-radio">
                  {selected === option && <div className="radio-selected" />}
                </div>
              </div>
            )
          })}
        </div>

        <div className="payment-gateway-actions">
          <button className="select-gateway-btn" onClick={handleSelect}>
            Continue with {gatewayInfo[selected]?.name}
          </button>
        </div>
      </div>
    </div>
  )
}

export default PaymentGatewaySelector
