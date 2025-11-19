import { useState } from 'react'
import './PaymentGatewaySelector.css'

function PaymentGatewaySelector({ question, options, onSelect }) {
  const [selected, setSelected] = useState(null)

  const icons = {
    stripe: '💳',
    paypal: '🅿️',
    razorpay: '💸',
    none: '⏭️'
  }

  return (
    <div className="gateway-modal-glass">
      <div className="gateway-header">
        <div className="header-icon">💰</div>
        <h3>{question}</h3>
        <p>Select integration method for your project</p>
      </div>
      
      <div className="gateway-grid">
        {options.map(opt => (
          <button 
            key={opt}
            className={`gateway-card ${selected === opt ? 'selected' : ''}`}
            onClick={() => setSelected(opt)}
          >
            <div className="card-icon">{icons[opt.toLowerCase()] || '💲'}</div>
            <div className="card-name">{opt}</div>
            <div className="card-select-indicator"></div>
          </button>
        ))}
      </div>

      <button 
        className="confirm-btn"
        disabled={!selected}
        onClick={() => onSelect(selected)}
      >
        Confirm Integration
      </button>
    </div>
  )
}

export default PaymentGatewaySelector