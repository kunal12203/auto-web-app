import { useState } from 'react'
import './TemplateSelector.css'

function TemplateSelector({ onSelectTemplate, onClose }) {
  const [selectedCategory, setSelectedCategory] = useState('All')

  const templates = [
    {
      id: 'modern-landing',
      name: 'Modern Landing Page',
      category: 'Landing Page',
      description: 'Clean, modern landing page with hero section, features, and CTA',
      icon: '🚀'
    },
    {
      id: 'portfolio',
      name: 'Portfolio Website',
      category: 'Portfolio',
      description: 'Professional portfolio with projects grid and about section',
      icon: '💼'
    },
    {
      id: 'saas-landing',
      name: 'SaaS Product Landing',
      category: 'Landing Page',
      description: 'Modern SaaS landing page with pricing and features',
      icon: '💻'
    },
    {
      id: 'restaurant',
      name: 'Restaurant Website',
      category: 'Business',
      description: 'Restaurant website with menu and contact section',
      icon: '🍽️'
    },
    {
      id: 'blog',
      name: 'Blog Website',
      category: 'Blog',
      description: 'Clean blog layout with article cards and categories',
      icon: '📝'
    },
    {
      id: 'ecommerce',
      name: 'E-Commerce Store',
      category: 'E-Commerce',
      description: 'Product showcase with shopping features',
      icon: '🛒'
    },
    {
      id: 'agency',
      name: 'Digital Agency',
      category: 'Business',
      description: 'Professional agency website with services and team',
      icon: '🎨'
    },
    {
      id: 'fitness',
      name: 'Fitness Gym',
      category: 'Health & Fitness',
      description: 'Gym and fitness center website',
      icon: '💪'
    },
    {
      id: 'photography',
      name: 'Photography Studio',
      category: 'Creative',
      description: 'Photography portfolio with gallery',
      icon: '📷'
    },
    {
      id: 'consulting',
      name: 'Business Consulting',
      category: 'Business',
      description: 'Professional consulting firm website',
      icon: '📊'
    },
    {
      id: 'education',
      name: 'Online Education',
      category: 'Education',
      description: 'Online learning platform website',
      icon: '📚'
    },
    {
      id: 'event',
      name: 'Event Conference',
      category: 'Events',
      description: 'Conference and event website',
      icon: '🎤'
    }
  ]

  const categories = ['All', 'Landing Page', 'Portfolio', 'Business', 'Blog', 'E-Commerce', 'Creative', 'Health & Fitness', 'Education', 'Events']

  const filteredTemplates = selectedCategory === 'All'
    ? templates
    : templates.filter(t => t.category === selectedCategory)

  const handleSelectTemplate = (templateId) => {
    onSelectTemplate(templateId)
    onClose()
  }

  return (
    <div className="template-selector-overlay">
      <div className="template-selector">
        <div className="template-selector-header">
          <h2>Choose a Template</h2>
          <button className="close-btn" onClick={onClose}>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>

        <div className="template-categories">
          {categories.map(category => (
            <button
              key={category}
              className={`category-btn ${selectedCategory === category ? 'active' : ''}`}
              onClick={() => setSelectedCategory(category)}
            >
              {category}
            </button>
          ))}
        </div>

        <div className="templates-grid">
          {filteredTemplates.map(template => (
            <div
              key={template.id}
              className="template-card"
              onClick={() => handleSelectTemplate(template.id)}
            >
              <div className="template-icon">{template.icon}</div>
              <h3>{template.name}</h3>
              <p className="template-category">{template.category}</p>
              <p className="template-description">{template.description}</p>
              <button className="select-template-btn">
                Select Template
              </button>
            </div>
          ))}
        </div>

        <div className="template-selector-footer">
          <p>Select a template to get started, then customize it with your own content!</p>
        </div>
      </div>
    </div>
  )
}

export default TemplateSelector
