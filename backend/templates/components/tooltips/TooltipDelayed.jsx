import { useState, useEffect, useRef } from 'react'

export default function DelayedTooltip({ children, content, delay = 500 }) {
  const [isVisible, setIsVisible] = useState(false)
  const timerRef = useRef(null)

  const handleMouseEnter = () => {
    timerRef.current = setTimeout(() => setIsVisible(true), delay)
  }

  const handleMouseLeave = () => {
    clearTimeout(timerRef.current)
    setIsVisible(false)
  }

  return (
    <div className="tooltip-container" onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>
      {children}
      {isVisible && <div className="tooltip">{content}</div>}
    </div>
  )
}