import { useEffect, useState } from 'react'
import './BuildingAnimation.css'

function BuildingAnimation({ message, stage, totalStages }) {
  const [terminalLines, setTerminalLines] = useState([])

  useEffect(() => {
    const newLine = `> ${message}... [${new Date().toLocaleTimeString()}]`
    setTerminalLines(prev => [...prev.slice(-4), newLine])
  }, [message])

  return (
    <div className="cinematic-overlay">
      <div className="hacker-terminal">
        <div className="terminal-header">
          <div className="dots">
            <span className="dot red"></span>
            <span className="dot yellow"></span>
            <span className="dot green"></span>
          </div>
          <span>AI_BUILD_PROCESS.EXE</span>
        </div>
        <div className="terminal-body">
          {terminalLines.map((line, i) => (
            <div key={i} className="terminal-line">{line}</div>
          ))}
          <div className="loading-bar-container">
             <div className="loading-bar" style={{ width: `${(stage / totalStages) * 100}%` }}></div>
          </div>
          <div className="status-blink">AWAITING INPUT_</div>
        </div>
      </div>
    </div>
  )
}

export default BuildingAnimation