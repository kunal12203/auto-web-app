import { useState } from 'react'

export default function InteractiveTooltip({ children, content }) {
  const [isVisible, setIsVisible] = useState(false)

  return (
    <div className="tooltip-container">
      <div
        onMouseEnter={() => setIsVisible(true)}
        onMouseLeave={() => setIsVisible(false)}
      >
        {children}
      </div>
      {isVisible && (
        <div className="tooltip interactive-tooltip" onMouseEnter={() => setIsVisible(true)}>
          {content}
        </div>
      )}
    </div>
  )
}