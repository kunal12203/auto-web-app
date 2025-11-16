import { useState } from 'react'
import './PromptInput.css'

function PromptInput({ onGenerate, disabled }) {
  const [inputValue, setInputValue] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (inputValue.trim() && !disabled) {
      onGenerate(inputValue)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSubmit(e)
    }
  }

  const examplePrompts = [
    "A modern landing page for a tech startup with hero section, features, pricing, and contact form with smooth scrolling navigation",
    "A portfolio website for a photographer with animated gallery grid, about section, and contact page using hash navigation",
    "A sleek SaaS product landing page with gradient backgrounds, feature cards, testimonials, and FAQ section",
    "An interactive restaurant website with menu navigation, image gallery, reservation form, and location map",
    "A personal blog homepage with article cards, categories navigation, search functionality, and newsletter signup"
  ]

  const handleExampleClick = (example) => {
    setInputValue(example)
  }

  return (
    <div className="prompt-input-container">
      <form onSubmit={handleSubmit} className="prompt-form">
        <label htmlFor="prompt">Describe your website:</label>
        <textarea
          id="prompt"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="E.g., A modern landing page for a tech startup with a hero section, features, and contact form..."
          rows="6"
          disabled={disabled}
        />
        <button type="submit" disabled={disabled || !inputValue.trim()}>
          {disabled ? 'Connecting...' : 'Generate Website'}
        </button>
      </form>

      <div className="examples">
        <h3>Example Prompts:</h3>
        <div className="example-list">
          {examplePrompts.map((example, index) => (
            <button
              key={index}
              className="example-button"
              onClick={() => handleExampleClick(example)}
              disabled={disabled}
            >
              {example}
            </button>
          ))}
        </div>
      </div>
    </div>
  )
}

export default PromptInput
