// TemplateSelector.jsx
import './TemplateSelector.css'
export default function TemplateSelector({ onSelect, onClose }) {
  const templates = [
    { id: 'landing', name: 'SaaS Landing', icon: '🚀' },
    { id: 'portfolio', name: 'Portfolio', icon: '💼' },
    { id: 'blog', name: 'Tech Blog', icon: '📝' },
    { id: 'ecommerce', name: 'Shop', icon: '🛍️' }
  ]
  return (
    <div className="template-modal">
      <div className="template-grid">
        {templates.map(t => (
          <div key={t.id} className="template-card" onClick={() => onSelect(t.id)}>
            <div className="t-icon">{t.icon}</div>
            <div className="t-name">{t.name}</div>
          </div>
        ))}
      </div>
      <button className="close-btn" onClick={onClose}>Close</button>
    </div>
  )
}