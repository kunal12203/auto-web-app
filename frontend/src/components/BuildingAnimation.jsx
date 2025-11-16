import { useEffect, useState } from 'react'
import './BuildingAnimation.css'

function BuildingAnimation({ message, stage, totalStages }) {
  const [dots, setDots] = useState('')

  useEffect(() => {
    const interval = setInterval(() => {
      setDots(prev => prev.length >= 3 ? '' : prev + '.')
    }, 500)

    return () => clearInterval(interval)
  }, [])

  const buildingStages = [
    { icon: '🔍', text: 'Analyzing your requirements', color: '#667eea' },
    { icon: '💡', text: 'Choosing best architecture', color: '#48bb78' },
    { icon: '⚙️', text: 'Generating project structure', color: '#ed8936' },
    { icon: '📝', text: 'Writing code with AI', color: '#9f7aea' },
    { icon: '🎨', text: 'Crafting beautiful UI', color: '#f687b3' },
    { icon: '🐳', text: 'Setting up Docker', color: '#4299e1' },
    { icon: '🔒', text: 'Configuring security', color: '#38b2ac' },
    { icon: '✨', text: 'Polishing final touches', color: '#ecc94b' },
  ]

  const currentStage = buildingStages[Math.min(stage || 0, buildingStages.length - 1)]

  return (
    <div className="building-animation">
      <div className="building-backdrop"></div>
      <div className="building-content">
        {/* Animated Logo */}
        <div className="building-logo">
          <div className="logo-ring"></div>
          <div className="logo-ring ring-2"></div>
          <div className="logo-ring ring-3"></div>
          <div className="logo-center" style={{ background: currentStage.color }}>
            <span className="building-icon">{currentStage.icon}</span>
          </div>
        </div>

        {/* Progress Text */}
        <div className="building-text">
          <h2>{message || currentStage.text}{dots}</h2>
          <p className="building-subtitle">Creating production-ready code</p>
        </div>

        {/* Progress Bar */}
        {totalStages && (
          <div className="building-progress">
            <div className="progress-bar">
              <div
                className="progress-fill"
                style={{
                  width: `${((stage + 1) / totalStages) * 100}%`,
                  background: currentStage.color
                }}
              ></div>
            </div>
            <div className="progress-text">
              Step {stage + 1} of {totalStages}
            </div>
          </div>
        )}

        {/* Code Lines Animation */}
        <div className="code-lines">
          {[...Array(5)].map((_, i) => (
            <div
              key={i}
              className="code-line"
              style={{ animationDelay: `${i * 0.2}s` }}
            >
              <div className="line-content" style={{ width: `${60 + Math.random() * 40}%` }}></div>
            </div>
          ))}
        </div>

        {/* Feature Tags */}
        <div className="building-features">
          <span className="feature-tag">🚀 Fast</span>
          <span className="feature-tag">🎨 Beautiful</span>
          <span className="feature-tag">📱 Responsive</span>
          <span className="feature-tag">🐳 Dockerized</span>
        </div>
      </div>
    </div>
  )
}

export default BuildingAnimation
