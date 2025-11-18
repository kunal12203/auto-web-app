import { useState } from 'react'

export default function ThemeToggle() {
  const [isDark, setIsDark] = useState(false)

  const toggleTheme = () => {
    setIsDark(!isDark)
    document.body.classList.toggle('dark-mode')
  }

  return (
    <button className="theme-toggle" onClick={toggleTheme}>
      {isDark ? '☀️' : '🌙'}
    </button>
  )
}