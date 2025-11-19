import { useState } from 'react'
import './PromptInput.css'

function PromptInput({ onGenerate, disabled, hasExistingWebsite }) {
  const [inputValue, setInputValue] = useState('')

  const handleSubmit = (e, isModification = false) => {
    e.preventDefault()
    if (inputValue.trim() && !disabled) {
      onGenerate(inputValue, isModification)
      if (isModification) setInputValue('')
    }
  }

  const suggestions = [
    "Portfolio for a Cyberpunk Artist",
    "SaaS Landing Page with Dark Mode",
    "Minimalist Coffee Shop Blog",
    "Crypto Dashboard with Charts"
  ]

  return (
    <div className="prompt-container">
      <form onSubmit={(e) => handleSubmit(e, false)} className="prompt-box">
        <div className="prompt-header">
          <span className="prompt-icon">✨</span>
          <span className="prompt-label">{hasExistingWebsite ? 'Iterate & Improve' : 'Create New'}</span>
        </div>
        
        <textarea
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && !e.shiftKey && handleSubmit(e, false)}
          placeholder="Describe your vision... (e.g., 'A futuristic landing page for an AI startup')"
          disabled={disabled}
        />
        
        <div className="prompt-footer">
          <div className="suggestions">
            {suggestions.map((s, i) => (
              <button key={i} type="button" onClick={() => setInputValue(s)} disabled={disabled}>
                {s}
              </button>
            ))}
          </div>
          <button type="submit" className="generate-btn" disabled={disabled || !inputValue.trim()}>
            {disabled ? 'Building...' : 'Generate'}
          </button>
        </div>
      </form>
    </div>
  )
}

export default PromptInput