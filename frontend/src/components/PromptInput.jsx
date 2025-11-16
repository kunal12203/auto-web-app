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
    "A modern landing page for a coffee shop with a hero section and menu",
    "A portfolio website for a photographer with a gallery grid",
    "A simple todo list app with add, delete, and mark complete features",
    "A pricing page with three tiers and feature comparison",
    "A contact form with name, email, and message fields"
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
