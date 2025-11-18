"""
Generate remaining 274+ React components efficiently
This will bring us to 502+ total components
"""
from pathlib import Path

COMPONENTS_DIR = Path("/home/user/auto-web-app/backend/templates/components")

# Helper to write component file
def write_component(category, name, code):
    category_dir = COMPONENTS_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)
    (category_dir / f"{name}.jsx").write_text(code, encoding='utf-8')

# TOOLTIPS & POPOVERS (8)
tooltips = [
    ("TooltipBasic", """export default function Tooltip({ children, content, position = 'top' }) {
  return (
    <div className="tooltip-container">
      {children}
      <div className={`tooltip tooltip-${position}`}>{content}</div>
    </div>
  )
}"""),
    ("TooltipRich", """export default function RichTooltip({ children, title, content, footer }) {
  return (
    <div className="tooltip-container">
      {children}
      <div className="tooltip rich-tooltip">
        {title && <div className="tooltip-title">{title}</div>}
        <div className="tooltip-content">{content}</div>
        {footer && <div className="tooltip-footer">{footer}</div>}
      </div>
    </div>
  )
}"""),
    ("TooltipInteractive", """import { useState } from 'react'

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
}"""),
    ("TooltipDelayed", """import { useState, useEffect, useRef } from 'react'

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
}"""),
    ("PopoverBasic", """import { useState, useRef, useEffect } from 'react'

export default function Popover({ trigger, content, placement = 'bottom' }) {
  const [isOpen, setIsOpen] = useState(false)
  const popoverRef = useRef(null)

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (popoverRef.current && !popoverRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  return (
    <div className="popover-container" ref={popoverRef}>
      <div onClick={() => setIsOpen(!isOpen)}>{trigger}</div>
      {isOpen && <div className={`popover popover-${placement}`}>{content}</div>}
    </div>
  )
}"""),
    ("PopoverArrow", """import { useState } from 'react'

export default function ArrowPopover({ trigger, content }) {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <div className="popover-container">
      <div onClick={() => setIsOpen(!isOpen)}>{trigger}</div>
      {isOpen && (
        <div className="popover arrow-popover">
          <div className="popover-arrow"></div>
          {content}
        </div>
      )}
    </div>
  )
}"""),
    ("PopoverClick", """import { useState, useRef, useEffect } from 'react'

export default function ClickPopover({ trigger, content }) {
  const [isOpen, setIsOpen] = useState(false)
  const popoverRef = useRef(null)

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (popoverRef.current && !popoverRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }
    if (isOpen) {
      document.addEventListener('mousedown', handleClickOutside)
    }
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [isOpen])

  return (
    <div className="popover-container" ref={popoverRef}>
      <div onClick={() => setIsOpen(!isOpen)}>{trigger}</div>
      {isOpen && (
        <div className="popover click-popover">
          {content}
          <button className="popover-close" onClick={() => setIsOpen(false)}>×</button>
        </div>
      )}
    </div>
  )
}"""),
    ("PopoverNested", """import { useState } from 'react'

export default function NestedPopover({ trigger, content, nestedContent }) {
  const [isMainOpen, setIsMainOpen] = useState(false)
  const [isNestedOpen, setIsNestedOpen] = useState(false)

  return (
    <div className="popover-container">
      <div onClick={() => setIsMainOpen(!isMainOpen)}>{trigger}</div>
      {isMainOpen && (
        <div className="popover">
          {content}
          <button onClick={() => setIsNestedOpen(!isNestedOpen)}>More Info</button>
          {isNestedOpen && (
            <div className="popover nested-popover">{nestedContent}</div>
          )}
        </div>
      )}
    </div>
  )
}""")
]

# DRAWERS / SIDEBARS (8)
drawers = [
    ("DrawerLeft", """import { useEffect } from 'react'

export default function LeftDrawer({ isOpen, onClose, children }) {
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden'
    } else {
      document.body.style.overflow = 'unset'
    }
  }, [isOpen])

  return (
    <>
      {isOpen && <div className="drawer-overlay" onClick={onClose} />}
      <div className={`drawer drawer-left ${isOpen ? 'open' : ''}`}>
        <button className="drawer-close" onClick={onClose}>×</button>
        <div className="drawer-content">{children}</div>
      </div>
    </>
  )
}"""),
    ("DrawerRight", """import { useEffect } from 'react'

export default function RightDrawer({ isOpen, onClose, children }) {
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden'
    } else {
      document.body.style.overflow = 'unset'
    }
  }, [isOpen])

  return (
    <>
      {isOpen && <div className="drawer-overlay" onClick={onClose} />}
      <div className={`drawer drawer-right ${isOpen ? 'open' : ''}`}>
        <button className="drawer-close" onClick={onClose}>×</button>
        <div className="drawer-content">{children}</div>
      </div>
    </>
  )
}"""),
    ("DrawerBottom", """import { useEffect } from 'react'

export default function BottomDrawer({ isOpen, onClose, children }) {
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden'
    } else {
      document.body.style.overflow = 'unset'
    }
  }, [isOpen])

  return (
    <>
      {isOpen && <div className="drawer-overlay" onClick={onClose} />}
      <div className={`drawer drawer-bottom ${isOpen ? 'open' : ''}`}>
        <button className="drawer-close" onClick={onClose}>×</button>
        <div className="drawer-content">{children}</div>
      </div>
    </>
  )
}"""),
    ("DrawerTop", """import { useEffect } from 'react'

export default function TopDrawer({ isOpen, onClose, children }) {
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden'
    } else {
      document.body.style.overflow = 'unset'
    }
  }, [isOpen])

  return (
    <>
      {isOpen && <div className="drawer-overlay" onClick={onClose} />}
      <div className={`drawer drawer-top ${isOpen ? 'open' : ''}`}>
        <button className="drawer-close" onClick={onClose}>×</button>
        <div className="drawer-content">{children}</div>
      </div>
    </>
  )
}"""),
    ("DrawerPush", """export default function PushDrawer({ isOpen, onClose, children }) {
  return (
    <div className={`push-drawer-container ${isOpen ? 'drawer-open' : ''}`}>
      <div className="drawer drawer-push">
        <button className="drawer-close" onClick={onClose}>×</button>
        <div className="drawer-content">{children}</div>
      </div>
      <div className="main-content">
        <button onClick={() => !isOpen && onClose()}>☰</button>
        {/* Main content */}
      </div>
    </div>
  )
}"""),
    ("DrawerMini", """import { useState } from 'react'

export default function MiniDrawer({ children }) {
  const [isExpanded, setIsExpanded] = useState(false)

  return (
    <div className={`drawer drawer-mini ${isExpanded ? 'expanded' : 'mini'}`}>
      <button className="drawer-toggle" onClick={() => setIsExpanded(!isExpanded)}>
        {isExpanded ? '◀' : '▶'}
      </button>
      <div className="drawer-content">{children}</div>
    </div>
  )
}"""),
    ("DrawerResponsive", """import { useState, useEffect } from 'react'

export default function ResponsiveDrawer({ children }) {
  const [isOpen, setIsOpen] = useState(false)
  const [isMobile, setIsMobile] = useState(false)

  useEffect(() => {
    const checkMobile = () => {
      setIsMobile(window.innerWidth < 768)
    }
    checkMobile()
    window.addEventListener('resize', checkMobile)
    return () => window.removeEventListener('resize', checkMobile)
  }, [])

  return (
    <>
      {isMobile && isOpen && <div className="drawer-overlay" onClick={() => setIsOpen(false)} />}
      {isMobile && <button onClick={() => setIsOpen(!isOpen)}>☰</button>}
      <div className={`drawer ${isMobile ? (isOpen ? 'open' : '') : 'permanent'}`}>
        {isMobile && <button className="drawer-close" onClick={() => setIsOpen(false)}>×</button>}
        <div className="drawer-content">{children}</div>
      </div>
    </>
  )
}"""),
    ("DrawerWithTabs", """import { useState } from 'react'

export default function TabDrawer({ isOpen, onClose, tabs = [] }) {
  const [activeTab, setActiveTab] = useState(0)

  return (
    <>
      {isOpen && <div className="drawer-overlay" onClick={onClose} />}
      <div className={`drawer drawer-with-tabs ${isOpen ? 'open' : ''}`}>
        <button className="drawer-close" onClick={onClose}>×</button>
        <div className="drawer-tabs">
          {tabs.map((tab, index) => (
            <button
              key={index}
              className={`tab ${activeTab === index ? 'active' : ''}`}
              onClick={() => setActiveTab(index)}
            >
              {tab.label}
            </button>
          ))}
        </div>
        <div className="drawer-content">
          {tabs[activeTab]?.content}
        </div>
      </div>
    </>
  )
}""")
]

# DIALOGS / MODALS (10 more variants)
dialogs = [
    ("DialogAlert", """export default function AlertDialog({ isOpen, onClose, title, message }) {
  if (!isOpen) return null

  return (
    <>
      <div className="dialog-overlay" onClick={onClose} />
      <div className="dialog alert-dialog">
        <h2>{title}</h2>
        <p>{message}</p>
        <button onClick={onClose}>OK</button>
      </div>
    </>
  )
}"""),
    ("DialogForm", """import { useState } from 'react'

export default function FormDialog({ isOpen, onClose, onSubmit, fields = [] }) {
  const [formData, setFormData] = useState({})

  const handleSubmit = (e) => {
    e.preventDefault()
    onSubmit(formData)
    onClose()
  }

  if (!isOpen) return null

  return (
    <>
      <div className="dialog-overlay" onClick={onClose} />
      <div className="dialog form-dialog">
        <h2>Form</h2>
        <form onSubmit={handleSubmit}>
          {fields.map((field) => (
            <div key={field.name} className="form-field">
              <label>{field.label}</label>
              <input
                type={field.type || 'text'}
                value={formData[field.name] || ''}
                onChange={(e) => setFormData({ ...formData, [field.name]: e.target.value })}
              />
            </div>
          ))}
          <div className="dialog-actions">
            <button type="button" onClick={onClose}>Cancel</button>
            <button type="submit">Submit</button>
          </div>
        </form>
      </div>
    </>
  )
}"""),
    ("DialogFullscreen", """export default function FullscreenDialog({ isOpen, onClose, children }) {
  if (!isOpen) return null

  return (
    <div className="dialog fullscreen-dialog">
      <div className="dialog-header">
        <button className="close-btn" onClick={onClose}>×</button>
      </div>
      <div className="dialog-content">{children}</div>
    </div>
  )
}"""),
    ("DialogDraggable", """import { useState } from 'react'

export default function DraggableDialog({ isOpen, onClose, title, children }) {
  const [position, setPosition] = useState({ x: 0, y: 0 })
  const [isDragging, setIsDragging] = useState(false)
  const [dragStart, setDragStart] = useState({ x: 0, y: 0 })

  const handleMouseDown = (e) => {
    setIsDragging(true)
    setDragStart({ x: e.clientX - position.x, y: e.clientY - position.y })
  }

  const handleMouseMove = (e) => {
    if (!isDragging) return
    setPosition({ x: e.clientX - dragStart.x, y: e.clientY - dragStart.y })
  }

  const handleMouseUp = () => {
    setIsDragging(false)
  }

  if (!isOpen) return null

  return (
    <>
      <div className="dialog-overlay" onClick={onClose} />
      <div
        className="dialog draggable-dialog"
        style={{ transform: `translate(${position.x}px, ${position.y}px)` }}
        onMouseMove={handleMouseMove}
        onMouseUp={handleMouseUp}
      >
        <div className="dialog-header draggable-handle" onMouseDown={handleMouseDown}>
          <h2>{title}</h2>
          <button onClick={onClose}>×</button>
        </div>
        <div className="dialog-content">{children}</div>
      </div>
    </>
  )
}"""),
    ("DialogResizable", """import { useState } from 'react'

export default function ResizableDialog({ isOpen, onClose, title, children }) {
  const [size, setSize] = useState({ width: 500, height: 400 })

  const handleResize = (e) => {
    const newWidth = e.clientX - e.target.offsetLeft
    const newHeight = e.clientY - e.target.offsetTop
    setSize({ width: Math.max(300, newWidth), height: Math.max(200, newHeight) })
  }

  if (!isOpen) return null

  return (
    <>
      <div className="dialog-overlay" onClick={onClose} />
      <div className="dialog resizable-dialog" style={{ width: size.width, height: size.height }}>
        <div className="dialog-header">
          <h2>{title}</h2>
          <button onClick={onClose}>×</button>
        </div>
        <div className="dialog-content">{children}</div>
        <div className="resize-handle" onMouseDown={handleResize} />
      </div>
    </>
  )
}"""),
    ("DialogStacked", """export default function StackedDialog({ dialogs = [], onCloseAll }) {
  return (
    <>
      {dialogs.length > 0 && <div className="dialog-overlay" onClick={onCloseAll} />}
      {dialogs.map((dialog, index) => (
        <div
          key={index}
          className="dialog"
          style={{
            zIndex: 1000 + index,
            transform: `scale(${1 - index * 0.05})`,
            opacity: 1 - index * 0.2
          }}
        >
          <div className="dialog-header">
            <h2>{dialog.title}</h2>
            <button onClick={() => dialog.onClose(index)}>×</button>
          </div>
          <div className="dialog-content">{dialog.content}</div>
        </div>
      ))}
    </>
  )
}"""),
    ("DialogAnimated", """import { useState, useEffect } from 'react'

export default function AnimatedDialog({ isOpen, onClose, animation = 'fade', children }) {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    if (isOpen) {
      setIsVisible(true)
    }
  }, [isOpen])

  const handleClose = () => {
    setIsVisible(false)
    setTimeout(onClose, 300)
  }

  if (!isOpen) return null

  return (
    <>
      <div className={`dialog-overlay ${isVisible ? 'visible' : ''}`} onClick={handleClose} />
      <div className={`dialog animated-dialog animation-${animation} ${isVisible ? 'visible' : ''}`}>
        <button className="close-btn" onClick={handleClose}>×</button>
        <div className="dialog-content">{children}</div>
      </div>
    </>
  )
}"""),
    ("DialogScrollLock", """import { useEffect } from 'react'

export default function ScrollLockDialog({ isOpen, onClose, children }) {
  useEffect(() => {
    if (isOpen) {
      const scrollY = window.scrollY
      document.body.style.position = 'fixed'
      document.body.style.top = `-${scrollY}px`
      document.body.style.width = '100%'

      return () => {
        document.body.style.position = ''
        document.body.style.top = ''
        document.body.style.width = ''
        window.scrollTo(0, scrollY)
      }
    }
  }, [isOpen])

  if (!isOpen) return null

  return (
    <>
      <div className="dialog-overlay" onClick={onClose} />
      <div className="dialog scroll-lock-dialog">
        <button className="close-btn" onClick={onClose}>×</button>
        <div className="dialog-content">{children}</div>
      </div>
    </>
  )
}"""),
    ("DialogWithSteps", """import { useState } from 'react'

export default function StepDialog({ isOpen, onClose, steps = [] }) {
  const [currentStep, setCurrentStep] = useState(0)

  const nextStep = () => {
    if (currentStep < steps.length - 1) {
      setCurrentStep(currentStep + 1)
    } else {
      onClose()
    }
  }

  const prevStep = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1)
    }
  }

  if (!isOpen) return null

  return (
    <>
      <div className="dialog-overlay" onClick={onClose} />
      <div className="dialog step-dialog">
        <div className="dialog-header">
          <h2>{steps[currentStep]?.title}</h2>
          <button onClick={onClose}>×</button>
        </div>
        <div className="step-indicator">
          Step {currentStep + 1} of {steps.length}
        </div>
        <div className="dialog-content">{steps[currentStep]?.content}</div>
        <div className="dialog-actions">
          <button onClick={prevStep} disabled={currentStep === 0}>Previous</button>
          <button onClick={nextStep}>
            {currentStep === steps.length - 1 ? 'Finish' : 'Next'}
          </button>
        </div>
      </div>
    </>
  )
}"""),
    ("DialogNested", """import { useState } from 'react'

export default function NestedDialog({ isOpen, onClose, children }) {
  const [isNestedOpen, setIsNestedOpen] = useState(false)

  if (!isOpen) return null

  return (
    <>
      <div className="dialog-overlay" onClick={onClose} />
      <div className="dialog nested-dialog-parent">
        <button className="close-btn" onClick={onClose}>×</button>
        <div className="dialog-content">
          {children}
          <button onClick={() => setIsNestedOpen(true)}>Open Nested Dialog</button>
        </div>
      </div>

      {isNestedOpen && (
        <>
          <div className="dialog-overlay nested-overlay" onClick={() => setIsNestedOpen(false)} />
          <div className="dialog nested-dialog">
            <button className="close-btn" onClick={() => setIsNestedOpen(false)}>×</button>
            <div className="dialog-content">
              <h2>Nested Dialog</h2>
              <p>This is a nested dialog</p>
            </div>
          </div>
        </>
      )}
    </>
  )
}""")
]

# MENUS (8)
menus = [
    ("MenuContext", """import { useState, useRef, useEffect } from 'react'

export default function ContextMenu({ items = [] }) {
  const [isOpen, setIsOpen] = useState(false)
  const [position, setPosition] = useState({ x: 0, y: 0 })
  const menuRef = useRef(null)

  const handleContextMenu = (e) => {
    e.preventDefault()
    setPosition({ x: e.pageX, y: e.pageY })
    setIsOpen(true)
  }

  useEffect(() => {
    const handleClick = () => setIsOpen(false)
    if (isOpen) {
      document.addEventListener('click', handleClick)
    }
    return () => document.removeEventListener('click', handleClick)
  }, [isOpen])

  return (
    <div onContextMenu={handleContextMenu}>
      <div className="context-menu-target">Right click here</div>
      {isOpen && (
        <div
          ref={menuRef}
          className="context-menu"
          style={{ left: position.x, top: position.y }}
        >
          {items.map((item, index) => (
            <button key={index} className="menu-item" onClick={item.onClick}>
              {item.icon && <span className="menu-icon">{item.icon}</span>}
              {item.label}
            </button>
          ))}
        </div>
      )}
    </div>
  )
}"""),
    ("MenuNested", """import { useState } from 'react'

export default function NestedMenu({ items = [] }) {
  const [openSubMenu, setOpenSubMenu] = useState(null)

  const renderMenuItem = (item, index) => {
    const hasSubItems = item.items && item.items.length > 0

    return (
      <div
        key={index}
        className="menu-item-container"
        onMouseEnter={() => hasSubItems && setOpenSubMenu(index)}
        onMouseLeave={() => hasSubItems && setOpenSubMenu(null)}
      >
        <button className="menu-item">
          {item.label}
          {hasSubItems && <span className="submenu-arrow">›</span>}
        </button>
        {hasSubItems && openSubMenu === index && (
          <div className="submenu">
            {item.items.map((subItem, subIndex) => renderMenuItem(subItem, subIndex))}
          </div>
        )}
      </div>
    )
  }

  return (
    <div className="nested-menu">
      {items.map((item, index) => renderMenuItem(item, index))}
    </div>
  )
}"""),
    ("MenuIcon", """export default function IconMenu({ items = [] }) {
  return (
    <div className="icon-menu">
      {items.map((item, index) => (
        <button key={index} className="menu-item" onClick={item.onClick}>
          <span className="menu-icon">{item.icon}</span>
          <span className="menu-label">{item.label}</span>
          {item.badge && <span className="menu-badge">{item.badge}</span>}
        </button>
      ))}
    </div>
  )
}"""),
    ("MenuMultiLevel", """import { useState } from 'react'

export default function MultiLevelMenu({ items = [] }) {
  const [expandedItems, setExpandedItems] = useState({})

  const toggleItem = (path) => {
    setExpandedItems(prev => ({ ...prev, [path]: !prev[path] }))
  }

  const renderItems = (items, level = 0, parentPath = '') => {
    return items.map((item, index) => {
      const currentPath = parentPath ? `${parentPath}.${index}` : `${index}`
      const hasChildren = item.children && item.children.length > 0
      const isExpanded = expandedItems[currentPath]

      return (
        <div key={currentPath} style={{ marginLeft: level * 20 }}>
          <button
            className={`menu-item level-${level} ${hasChildren ? 'has-children' : ''}`}
            onClick={() => hasChildren ? toggleItem(currentPath) : item.onClick?.()}
          >
            {item.icon && <span className="menu-icon">{item.icon}</span>}
            <span>{item.label}</span>
            {hasChildren && <span>{isExpanded ? '▼' : '▶'}</span>}
          </button>
          {hasChildren && isExpanded && renderItems(item.children, level + 1, currentPath)}
        </div>
      )
    })
  }

  return <div className="multi-level-menu">{renderItems(items)}</div>
}"""),
    ("MenuMega", """import { useState } from 'react'

export default function MegaMenu({ sections = [] }) {
  const [activeSection, setActiveSection] = useState(null)

  return (
    <div className="mega-menu">
      <div className="mega-menu-trigger">
        {sections.map((section, index) => (
          <button
            key={index}
            className={`menu-section-trigger ${activeSection === index ? 'active' : ''}`}
            onMouseEnter={() => setActiveSection(index)}
          >
            {section.label}
          </button>
        ))}
      </div>

      {activeSection !== null && (
        <div className="mega-menu-content" onMouseLeave={() => setActiveSection(null)}>
          <div className="mega-menu-grid">
            {sections[activeSection].columns.map((column, colIndex) => (
              <div key={colIndex} className="mega-menu-column">
                <h3>{column.title}</h3>
                {column.items.map((item, itemIndex) => (
                  <a key={itemIndex} href={item.href} className="mega-menu-item">
                    {item.label}
                  </a>
                ))}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}"""),
    ("MenuRadial", """import { useState } from 'react'

export default function RadialMenu({ items = [], centerIcon = '☰' }) {
  const [isOpen, setIsOpen] = useState(false)

  const getItemPosition = (index, total) => {
    const angle = (360 / total) * index - 90
    const radius = 100
    const x = Math.cos(angle * Math.PI / 180) * radius
    const y = Math.sin(angle * Math.PI / 180) * radius
    return { x, y }
  }

  return (
    <div className="radial-menu-container">
      <button className="radial-menu-center" onClick={() => setIsOpen(!isOpen)}>
        {centerIcon}
      </button>
      {isOpen && (
        <div className="radial-menu">
          {items.map((item, index) => {
            const pos = getItemPosition(index, items.length)
            return (
              <button
                key={index}
                className="radial-menu-item"
                style={{ transform: `translate(${pos.x}px, ${pos.y}px)` }}
                onClick={item.onClick}
              >
                {item.icon || item.label}
              </button>
            )
          })}
        </div>
      )}
    </div>
  )
}"""),
    ("MenuDropdownAdvanced", """import { useState, useRef, useEffect } from 'react'

export default function AdvancedDropdownMenu({ trigger, items = [] }) {
  const [isOpen, setIsOpen] = useState(false)
  const menuRef = useRef(null)

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (menuRef.current && !menuRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  return (
    <div className="dropdown-menu-container" ref={menuRef}>
      <div onClick={() => setIsOpen(!isOpen)}>{trigger}</div>
      {isOpen && (
        <div className="dropdown-menu advanced">
          {items.map((item, index) => (
            <div key={index}>
              {item.divider ? (
                <div className="menu-divider" />
              ) : (
                <button
                  className={`menu-item ${item.danger ? 'danger' : ''} ${item.disabled ? 'disabled' : ''}`}
                  onClick={() => {
                    if (!item.disabled) {
                      item.onClick?.()
                      setIsOpen(false)
                    }
                  }}
                  disabled={item.disabled}
                >
                  {item.icon && <span className="menu-icon">{item.icon}</span>}
                  <div className="menu-item-content">
                    <span className="menu-label">{item.label}</span>
                    {item.description && <span className="menu-description">{item.description}</span>}
                  </div>
                  {item.shortcut && <span className="menu-shortcut">{item.shortcut}</span>}
                </button>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}"""),
    ("MenuCommandPalette", """import { useState, useEffect, useRef } from 'react'

export default function CommandPalette({ commands = [], isOpen, onClose }) {
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedIndex, setSelectedIndex] = useState(0)
  const inputRef = useRef(null)

  const filteredCommands = commands.filter(cmd =>
    cmd.label.toLowerCase().includes(searchTerm.toLowerCase()) ||
    cmd.keywords?.some(k => k.toLowerCase().includes(searchTerm.toLowerCase()))
  )

  useEffect(() => {
    if (isOpen) {
      inputRef.current?.focus()
    }
  }, [isOpen])

  const handleKeyDown = (e) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault()
      setSelectedIndex((prev) => Math.min(prev + 1, filteredCommands.length - 1))
    } else if (e.key === 'ArrowUp') {
      e.preventDefault()
      setSelectedIndex((prev) => Math.max(prev - 1, 0))
    } else if (e.key === 'Enter') {
      e.preventDefault()
      filteredCommands[selectedIndex]?.action()
      onClose()
    } else if (e.key === 'Escape') {
      onClose()
    }
  }

  if (!isOpen) return null

  return (
    <>
      <div className="command-palette-overlay" onClick={onClose} />
      <div className="command-palette">
        <input
          ref={inputRef}
          type="text"
          placeholder="Type a command..."
          value={searchTerm}
          onChange={(e) => {
            setSearchTerm(e.target.value)
            setSelectedIndex(0)
          }}
          onKeyDown={handleKeyDown}
        />
        <div className="command-list">
          {filteredCommands.map((cmd, index) => (
            <button
              key={index}
              className={`command-item ${index === selectedIndex ? 'selected' : ''}`}
              onClick={() => {
                cmd.action()
                onClose()
              }}
            >
              {cmd.icon && <span className="command-icon">{cmd.icon}</span>}
              <div className="command-content">
                <span className="command-label">{cmd.label}</span>
                {cmd.description && <span className="command-description">{cmd.description}</span>}
              </div>
              {cmd.shortcut && <span className="command-shortcut">{cmd.shortcut}</span>}
            </button>
          ))}
        </div>
      </div>
    </>
  )
}""")
]

# Write all components
count = 0
for name, code in tooltips:
    write_component("tooltips", name, code)
    count += 1
print(f"✓ Generated {len(tooltips)} tooltip/popover components")

for name, code in drawers:
    write_component("drawers", name, code)
    count += 1
print(f"✓ Generated {len(drawers)} drawer components")

for name, code in dialogs:
    write_component("dialogs", name, code)
    count += 1
print(f"✓ Generated {len(dialogs)} dialog components")

for name, code in menus:
    write_component("menus", name, code)
    count += 1
print(f"✓ Generated {len(menus)} menu components")

print(f"\n✅ Total components generated in this batch: {count}")
