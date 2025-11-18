import { useState } from 'react'

export default function LanguageSelector() {
  const [language, setLanguage] = useState('en')

  return (
    <select
      className="language-selector"
      value={language}
      onChange={(e) => setLanguage(e.target.value)}
    >
      <option value="en">English</option>
      <option value="es">Español</option>
      <option value="fr">Français</option>
      <option value="de">Deutsch</option>
    </select>
  )
}