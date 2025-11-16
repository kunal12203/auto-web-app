import { useState } from 'react'
import './PromptInput.css'

function PromptInput({ onGenerate, disabled, hasExistingWebsite }) {
  const [inputValue, setInputValue] = useState('')

  const handleSubmit = (e, isModification = false) => {
    e.preventDefault()
    if (inputValue.trim() && !disabled) {
      onGenerate(inputValue, isModification)
      if (isModification) {
        setInputValue('')
      }
    }
  }

  const handleKeyPress = (e, isModification = false) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSubmit(e, isModification)
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
      {hasExistingWebsite && (
        <form onSubmit={(e) => handleSubmit(e, true)} className="prompt-form modify-form">
          <label htmlFor="modify-prompt">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
              <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
            </svg>
            Modify Website:
          </label>
          <textarea
            id="modify-prompt"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={(e) => handleKeyPress(e, true)}
            placeholder="E.g., Change the color scheme to blue, Add a testimonials section, Make the header sticky..."
            rows="3"
            disabled={disabled}
          />
          <button type="submit" disabled={disabled || !inputValue.trim()} className="modify-btn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
            Apply Changes
          </button>
        </form>
      )}

      <form onSubmit={(e) => handleSubmit(e, false)} className="prompt-form">
        <label htmlFor="prompt">{hasExistingWebsite ? 'Or create new website:' : 'Describe your website:'}</label>
        <textarea
          id="prompt"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={(e) => handleKeyPress(e, false)}
          placeholder="E.g., A modern landing page for a tech startup with a hero section, features, and contact form..."
          rows={hasExistingWebsite ? "4" : "6"}
          disabled={disabled}
        />
        <button type="submit" disabled={disabled || !inputValue.trim()}>
          {disabled ? 'Connecting...' : hasExistingWebsite ? 'Generate New Website' : 'Generate Website'}
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
