"""
Generate Advanced UI Components (60 templates)
- Accordions, Carousels, Dropdowns, Tooltips, Drawers, Dialogs, Menus
"""
from pathlib import Path

COMPONENTS_DIR = Path("/home/user/auto-web-app/backend/templates/components")

# Accordion variants (8)
accordions = {
    "AccordionBasic": """import { useState } from 'react'

export default function Accordion({ items = [] }) {
  const [openIndex, setOpenIndex] = useState(null)

  const defaultItems = [
    { title: '{{ACCORDION_ITEM_1_TITLE}}', content: '{{ACCORDION_ITEM_1_CONTENT}}' },
    { title: '{{ACCORDION_ITEM_2_TITLE}}', content: '{{ACCORDION_ITEM_2_CONTENT}}' },
    { title: '{{ACCORDION_ITEM_3_TITLE}}', content: '{{ACCORDION_ITEM_3_CONTENT}}' }
  ]

  const accordionItems = items.length > 0 ? items : defaultItems

  return (
    <div className="accordion">
      {accordionItems.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header ${openIndex === index ? 'active' : ''}`}
            onClick={() => setOpenIndex(openIndex === index ? null : index)}
          >
            <span>{item.title}</span>
            <span className="accordion-icon">{openIndex === index ? '−' : '+'}</span>
          </button>
          {openIndex === index && (
            <div className="accordion-content">{item.content}</div>
          )}
        </div>
      ))}
    </div>
  )
}""",

    "AccordionNested": """import { useState } from 'react'

export default function NestedAccordion({ items = [] }) {
  const [openIndexes, setOpenIndexes] = useState({})

  const toggleItem = (path) => {
    setOpenIndexes(prev => ({ ...prev, [path]: !prev[path] }))
  }

  const renderItems = (items, parentPath = '') => {
    return items.map((item, index) => {
      const currentPath = parentPath ? `${parentPath}.${index}` : `${index}`
      const isOpen = openIndexes[currentPath]

      return (
        <div key={currentPath} className="nested-accordion-item" style={{ marginLeft: parentPath ? '20px' : '0' }}>
          <button
            className={`accordion-header ${isOpen ? 'active' : ''}`}
            onClick={() => toggleItem(currentPath)}
          >
            {item.title}
            <span>{isOpen ? '−' : '+'}</span>
          </button>
          {isOpen && item.content && <div className="accordion-content">{item.content}</div>}
          {isOpen && item.children && renderItems(item.children, currentPath)}
        </div>
      )
    })
  }

  return <div className="nested-accordion">{renderItems(items)}</div>
}""",

    "AccordionMultiSelect": """import { useState } from 'react'

export default function MultiSelectAccordion({ items = [], allowMultiple = true }) {
  const [openIndexes, setOpenIndexes] = useState([])

  const toggleItem = (index) => {
    if (allowMultiple) {
      setOpenIndexes(prev =>
        prev.includes(index) ? prev.filter(i => i !== index) : [...prev, index]
      )
    } else {
      setOpenIndexes(prev => (prev.includes(index) ? [] : [index]))
    }
  }

  return (
    <div className="multi-select-accordion">
      {items.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header ${openIndexes.includes(index) ? 'active' : ''}`}
            onClick={() => toggleItem(index)}
          >
            {item.title}
            <span>{openIndexes.includes(index) ? '−' : '+'}</span>
          </button>
          {openIndexes.includes(index) && (
            <div className="accordion-content">{item.content}</div>
          )}
        </div>
      ))}
    </div>
  )
}""",

    "AccordionAnimated": """import { useState } from 'react'

export default function AnimatedAccordion({ items = [] }) {
  const [openIndex, setOpenIndex] = useState(null)

  return (
    <div className="animated-accordion">
      {items.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header ${openIndex === index ? 'active' : ''}`}
            onClick={() => setOpenIndex(openIndex === index ? null : index)}
          >
            <span>{item.title}</span>
            <span className="icon-rotate">{openIndex === index ? '−' : '+'}</span>
          </button>
          <div className={`accordion-content-wrapper ${openIndex === index ? 'open' : 'closed'}`}>
            <div className="accordion-content">{item.content}</div>
          </div>
        </div>
      ))}
    </div>
  )
}""",

    "AccordionWithIcons": """import { useState } from 'react'

export default function IconAccordion({ items = [] }) {
  const [openIndex, setOpenIndex] = useState(null)

  return (
    <div className="icon-accordion">
      {items.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header ${openIndex === index ? 'active' : ''}`}
            onClick={() => setOpenIndex(openIndex === index ? null : index)}
          >
            <span className="accordion-icon-left">{item.icon || '📄'}</span>
            <span>{item.title}</span>
            <span className="accordion-icon-right">{openIndex === index ? '▲' : '▼'}</span>
          </button>
          {openIndex === index && (
            <div className="accordion-content">{item.content}</div>
          )}
        </div>
      ))}
    </div>
  )
}""",

    "AccordionControlled": """import { useEffect, useState } from 'react'

export default function ControlledAccordion({ items = [], activeIndex = null, onChange }) {
  const [internalIndex, setInternalIndex] = useState(activeIndex)

  useEffect(() => {
    setInternalIndex(activeIndex)
  }, [activeIndex])

  const handleToggle = (index) => {
    const newIndex = internalIndex === index ? null : index
    setInternalIndex(newIndex)
    if (onChange) onChange(newIndex)
  }

  return (
    <div className="controlled-accordion">
      {items.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header ${internalIndex === index ? 'active' : ''}`}
            onClick={() => handleToggle(index)}
          >
            {item.title}
            <span>{internalIndex === index ? '−' : '+'}</span>
          </button>
          {internalIndex === index && (
            <div className="accordion-content">{item.content}</div>
          )}
        </div>
      ))}
    </div>
  )
}""",

    "AccordionSearchable": """import { useState } from 'react'

export default function SearchableAccordion({ items = [] }) {
  const [searchTerm, setSearchTerm] = useState('')
  const [openIndex, setOpenIndex] = useState(null)

  const filteredItems = items.filter(item =>
    item.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
    item.content.toLowerCase().includes(searchTerm.toLowerCase())
  )

  return (
    <div className="searchable-accordion">
      <input
        type="text"
        className="accordion-search"
        placeholder="Search..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      {filteredItems.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header ${openIndex === index ? 'active' : ''}`}
            onClick={() => setOpenIndex(openIndex === index ? null : index)}
          >
            {item.title}
            <span>{openIndex === index ? '−' : '+'}</span>
          </button>
          {openIndex === index && (
            <div className="accordion-content">{item.content}</div>
          )}
        </div>
      ))}
      {filteredItems.length === 0 && <div className="no-results">No results found</div>}
    </div>
  )
}""",

    "AccordionLazyLoad": """import { useState } from 'react'

export default function LazyAccordion({ items = [], onLoadContent }) {
  const [openIndex, setOpenIndex] = useState(null)
  const [loadedContent, setLoadedContent] = useState({})

  const handleToggle = async (index) => {
    if (openIndex === index) {
      setOpenIndex(null)
      return
    }

    setOpenIndex(index)

    if (!loadedContent[index] && onLoadContent) {
      const content = await onLoadContent(items[index])
      setLoadedContent(prev => ({ ...prev, [index]: content }))
    }
  }

  return (
    <div className="lazy-accordion">
      {items.map((item, index) => (
        <div key={index} className="accordion-item">
          <button
            className={`accordion-header ${openIndex === index ? 'active' : ''}`}
            onClick={() => handleToggle(index)}
          >
            {item.title}
            <span>{openIndex === index ? '−' : '+'}</span>
          </button>
          {openIndex === index && (
            <div className="accordion-content">
              {loadedContent[index] || item.content || 'Loading...'}
            </div>
          )}
        </div>
      ))}
    </div>
  )
}"""
}

# Carousel variants (10)
carousels = {
    "CarouselBasic": """import { useState } from 'react'

export default function Carousel({ items = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0)

  const defaultItems = [
    { image: '{{CAROUSEL_IMAGE_1}}', title: '{{CAROUSEL_TITLE_1}}', description: '{{CAROUSEL_DESC_1}}' },
    { image: '{{CAROUSEL_IMAGE_2}}', title: '{{CAROUSEL_TITLE_2}}', description: '{{CAROUSEL_DESC_2}}' },
    { image: '{{CAROUSEL_IMAGE_3}}', title: '{{CAROUSEL_TITLE_3}}', description: '{{CAROUSEL_DESC_3}}' }
  ]

  const slides = items.length > 0 ? items : defaultItems

  const next = () => setCurrentIndex((currentIndex + 1) % slides.length)
  const prev = () => setCurrentIndex((currentIndex - 1 + slides.length) % slides.length)

  return (
    <div className="carousel">
      <button className="carousel-btn prev" onClick={prev}>‹</button>
      <div className="carousel-slide">
        <div className="carousel-image">{slides[currentIndex].image}</div>
        <h3>{slides[currentIndex].title}</h3>
        <p>{slides[currentIndex].description}</p>
      </div>
      <button className="carousel-btn next" onClick={next}>›</button>
      <div className="carousel-indicators">
        {slides.map((_, index) => (
          <button
            key={index}
            className={`indicator ${index === currentIndex ? 'active' : ''}`}
            onClick={() => setCurrentIndex(index)}
          />
        ))}
      </div>
    </div>
  )
}""",

    "Carousel3D": """import { useState } from 'react'

export default function Carousel3D({ items = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0)

  const getTransform = (index) => {
    const diff = index - currentIndex
    const angle = diff * 60
    const translateZ = Math.abs(diff) === 0 ? 200 : 0
    return `rotateY(${angle}deg) translateZ(${translateZ}px)`
  }

  return (
    <div className="carousel-3d-container">
      <div className="carousel-3d">
        {items.map((item, index) => (
          <div
            key={index}
            className={`carousel-3d-item ${index === currentIndex ? 'active' : ''}`}
            style={{ transform: getTransform(index) }}
            onClick={() => setCurrentIndex(index)}
          >
            {item.content}
          </div>
        ))}
      </div>
      <div className="carousel-controls">
        <button onClick={() => setCurrentIndex((currentIndex - 1 + items.length) % items.length)}>‹</button>
        <button onClick={() => setCurrentIndex((currentIndex + 1) % items.length)}>›</button>
      </div>
    </div>
  )
}""",

    "CarouselAutoPlay": """import { useState, useEffect } from 'react'

export default function AutoPlayCarousel({ items = [], interval = 3000, pauseOnHover = true }) {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [isPaused, setIsPaused] = useState(false)

  useEffect(() => {
    if (isPaused) return

    const timer = setInterval(() => {
      setCurrentIndex((prev) => (prev + 1) % items.length)
    }, interval)

    return () => clearInterval(timer)
  }, [isPaused, interval, items.length])

  return (
    <div
      className="autoplay-carousel"
      onMouseEnter={() => pauseOnHover && setIsPaused(true)}
      onMouseLeave={() => pauseOnHover && setIsPaused(false)}
    >
      <div className="carousel-slide">{items[currentIndex]?.content}</div>
      <div className="carousel-indicators">
        {items.map((_, index) => (
          <button
            key={index}
            className={`indicator ${index === currentIndex ? 'active' : ''}`}
            onClick={() => setCurrentIndex(index)}
          />
        ))}
      </div>
    </div>
  )
}""",

    "CarouselThumbnail": """import { useState } from 'react'

export default function ThumbnailCarousel({ items = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0)

  return (
    <div className="thumbnail-carousel">
      <div className="main-slide">
        <img src={items[currentIndex]?.image || '{{MAIN_IMAGE}}'} alt={items[currentIndex]?.title} />
        <div className="slide-info">
          <h3>{items[currentIndex]?.title}</h3>
          <p>{items[currentIndex]?.description}</p>
        </div>
      </div>
      <div className="thumbnails">
        {items.map((item, index) => (
          <button
            key={index}
            className={`thumbnail ${index === currentIndex ? 'active' : ''}`}
            onClick={() => setCurrentIndex(index)}
          >
            <img src={item.thumbnail || item.image} alt={item.title} />
          </button>
        ))}
      </div>
    </div>
  )
}""",

    "CarouselVertical": """import { useState } from 'react'

export default function VerticalCarousel({ items = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0)

  const next = () => setCurrentIndex((currentIndex + 1) % items.length)
  const prev = () => setCurrentIndex((currentIndex - 1 + items.length) % items.length)

  return (
    <div className="vertical-carousel">
      <button className="carousel-btn up" onClick={prev}>▲</button>
      <div className="carousel-track" style={{ transform: `translateY(-${currentIndex * 100}%)` }}>
        {items.map((item, index) => (
          <div key={index} className="carousel-slide">
            {item.content}
          </div>
        ))}
      </div>
      <button className="carousel-btn down" onClick={next}>▼</button>
    </div>
  )
}""",

    "CarouselInfinite": """import { useState } from 'react'

export default function InfiniteCarousel({ items = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0)
  const extendedItems = [...items, ...items, ...items]

  const next = () => {
    setCurrentIndex((prev) => prev + 1)
    if (currentIndex >= items.length * 2) {
      setTimeout(() => setCurrentIndex(items.length), 300)
    }
  }

  const prev = () => {
    setCurrentIndex((prev) => prev - 1)
    if (currentIndex <= items.length) {
      setTimeout(() => setCurrentIndex(items.length * 2), 300)
    }
  }

  return (
    <div className="infinite-carousel">
      <button onClick={prev}>‹</button>
      <div className="carousel-viewport">
        <div className="carousel-track" style={{ transform: `translateX(-${currentIndex * 100}%)` }}>
          {extendedItems.map((item, index) => (
            <div key={index} className="carousel-slide">{item.content}</div>
          ))}
        </div>
      </div>
      <button onClick={next}>›</button>
    </div>
  )
}""",

    "CarouselFade": """import { useState, useEffect } from 'react'

export default function FadeCarousel({ items = [], duration = 4000 }) {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [fadeClass, setFadeClass] = useState('fade-in')

  useEffect(() => {
    const timer = setInterval(() => {
      setFadeClass('fade-out')
      setTimeout(() => {
        setCurrentIndex((prev) => (prev + 1) % items.length)
        setFadeClass('fade-in')
      }, 300)
    }, duration)

    return () => clearInterval(timer)
  }, [items.length, duration])

  return (
    <div className="fade-carousel">
      <div className={`carousel-slide ${fadeClass}`}>
        {items[currentIndex]?.content}
      </div>
    </div>
  )
}""",

    "CarouselZoom": """import { useState } from 'react'

export default function ZoomCarousel({ items = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [isZoomed, setIsZoomed] = useState(false)

  return (
    <div className="zoom-carousel">
      <div
        className={`carousel-slide ${isZoomed ? 'zoomed' : ''}`}
        onClick={() => setIsZoomed(!isZoomed)}
      >
        <img src={items[currentIndex]?.image} alt={items[currentIndex]?.title} />
      </div>
      <div className="carousel-controls">
        <button onClick={() => setCurrentIndex((currentIndex - 1 + items.length) % items.length)}>‹</button>
        <span>{currentIndex + 1} / {items.length}</span>
        <button onClick={() => setCurrentIndex((currentIndex + 1) % items.length)}>›</button>
      </div>
    </div>
  )
}""",

    "CarouselMultiItem": """import { useState } from 'react'

export default function MultiItemCarousel({ items = [], itemsPerSlide = 3 }) {
  const [currentIndex, setCurrentIndex] = useState(0)

  const totalSlides = Math.ceil(items.length / itemsPerSlide)

  const next = () => setCurrentIndex((currentIndex + 1) % totalSlides)
  const prev = () => setCurrentIndex((currentIndex - 1 + totalSlides) % totalSlides)

  const visibleItems = items.slice(
    currentIndex * itemsPerSlide,
    (currentIndex + 1) * itemsPerSlide
  )

  return (
    <div className="multi-item-carousel">
      <button className="carousel-btn prev" onClick={prev}>‹</button>
      <div className="carousel-items">
        {visibleItems.map((item, index) => (
          <div key={index} className="carousel-item">
            {item.content}
          </div>
        ))}
      </div>
      <button className="carousel-btn next" onClick={next}>›</button>
    </div>
  )
}""",

    "CarouselTouch": """import { useState, useRef } from 'react'

export default function TouchCarousel({ items = [] }) {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [touchStart, setTouchStart] = useState(0)
  const [touchEnd, setTouchEnd] = useState(0)

  const handleTouchStart = (e) => {
    setTouchStart(e.touches[0].clientX)
  }

  const handleTouchMove = (e) => {
    setTouchEnd(e.touches[0].clientX)
  }

  const handleTouchEnd = () => {
    if (touchStart - touchEnd > 50) {
      // Swipe left
      setCurrentIndex((prev) => (prev + 1) % items.length)
    }
    if (touchStart - touchEnd < -50) {
      // Swipe right
      setCurrentIndex((prev) => (prev - 1 + items.length) % items.length)
    }
  }

  return (
    <div
      className="touch-carousel"
      onTouchStart={handleTouchStart}
      onTouchMove={handleTouchMove}
      onTouchEnd={handleTouchEnd}
    >
      <div className="carousel-track" style={{ transform: `translateX(-${currentIndex * 100}%)` }}>
        {items.map((item, index) => (
          <div key={index} className="carousel-slide">
            {item.content}
          </div>
        ))}
      </div>
      <div className="carousel-indicators">
        {items.map((_, index) => (
          <span key={index} className={index === currentIndex ? 'active' : ''} />
        ))}
      </div>
    </div>
  )
}"""
}

# Dropdown variants (8)
dropdowns = {
    "DropdownBasic": """import { useState, useRef, useEffect } from 'react'

export default function Dropdown({ label = '{{DROPDOWN_LABEL}}', options = [] }) {
  const [isOpen, setIsOpen] = useState(false)
  const [selected, setSelected] = useState(null)
  const dropdownRef = useRef(null)

  const defaultOptions = [
    { value: '1', label: '{{OPTION_1}}' },
    { value: '2', label: '{{OPTION_2}}' },
    { value: '3', label: '{{OPTION_3}}' }
  ]

  const items = options.length > 0 ? options : defaultOptions

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  return (
    <div className="dropdown" ref={dropdownRef}>
      <button className="dropdown-trigger" onClick={() => setIsOpen(!isOpen)}>
        {selected ? selected.label : label}
        <span className="dropdown-arrow">{isOpen ? '▲' : '▼'}</span>
      </button>
      {isOpen && (
        <div className="dropdown-menu">
          {items.map((option) => (
            <button
              key={option.value}
              className="dropdown-item"
              onClick={() => {
                setSelected(option)
                setIsOpen(false)
              }}
            >
              {option.label}
            </button>
          ))}
        </div>
      )}
    </div>
  )
}""",

    "DropdownMultiSelect": """import { useState, useRef, useEffect } from 'react'

export default function MultiSelectDropdown({ label = 'Select items', options = [] }) {
  const [isOpen, setIsOpen] = useState(false)
  const [selected, setSelected] = useState([])
  const dropdownRef = useRef(null)

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  const toggleOption = (option) => {
    setSelected(prev =>
      prev.find(item => item.value === option.value)
        ? prev.filter(item => item.value !== option.value)
        : [...prev, option]
    )
  }

  return (
    <div className="multi-select-dropdown" ref={dropdownRef}>
      <button className="dropdown-trigger" onClick={() => setIsOpen(!isOpen)}>
        {selected.length > 0 ? `${selected.length} selected` : label}
        <span className="dropdown-arrow">{isOpen ? '▲' : '▼'}</span>
      </button>
      {isOpen && (
        <div className="dropdown-menu">
          {options.map((option) => (
            <label key={option.value} className="dropdown-item checkbox-item">
              <input
                type="checkbox"
                checked={selected.find(item => item.value === option.value) !== undefined}
                onChange={() => toggleOption(option)}
              />
              <span>{option.label}</span>
            </label>
          ))}
        </div>
      )}
      {selected.length > 0 && (
        <div className="selected-tags">
          {selected.map((item) => (
            <span key={item.value} className="tag">
              {item.label}
              <button onClick={() => toggleOption(item)}>×</button>
            </span>
          ))}
        </div>
      )}
    </div>
  )
}""",

    "DropdownSearchable": """import { useState, useRef, useEffect } from 'react'

export default function SearchableDropdown({ label = 'Search...', options = [] }) {
  const [isOpen, setIsOpen] = useState(false)
  const [searchTerm, setSearchTerm] = useState('')
  const [selected, setSelected] = useState(null)
  const dropdownRef = useRef(null)

  const filteredOptions = options.filter(option =>
    option.label.toLowerCase().includes(searchTerm.toLowerCase())
  )

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  return (
    <div className="searchable-dropdown" ref={dropdownRef}>
      <div className="dropdown-trigger">
        <input
          type="text"
          placeholder={selected ? selected.label : label}
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          onFocus={() => setIsOpen(true)}
        />
      </div>
      {isOpen && (
        <div className="dropdown-menu">
          {filteredOptions.length > 0 ? (
            filteredOptions.map((option) => (
              <button
                key={option.value}
                className="dropdown-item"
                onClick={() => {
                  setSelected(option)
                  setSearchTerm('')
                  setIsOpen(false)
                }}
              >
                {option.label}
              </button>
            ))
          ) : (
            <div className="dropdown-item no-results">No results found</div>
          )}
        </div>
      )}
    </div>
  )
}""",

    "DropdownGrouped": """import { useState, useRef, useEffect } from 'react'

export default function GroupedDropdown({ label = 'Select option', groups = [] }) {
  const [isOpen, setIsOpen] = useState(false)
  const [selected, setSelected] = useState(null)
  const dropdownRef = useRef(null)

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  return (
    <div className="grouped-dropdown" ref={dropdownRef}>
      <button className="dropdown-trigger" onClick={() => setIsOpen(!isOpen)}>
        {selected ? selected.label : label}
        <span>{isOpen ? '▲' : '▼'}</span>
      </button>
      {isOpen && (
        <div className="dropdown-menu">
          {groups.map((group, groupIndex) => (
            <div key={groupIndex} className="dropdown-group">
              <div className="group-label">{group.label}</div>
              {group.options.map((option) => (
                <button
                  key={option.value}
                  className="dropdown-item"
                  onClick={() => {
                    setSelected(option)
                    setIsOpen(false)
                  }}
                >
                  {option.label}
                </button>
              ))}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}""",

    "DropdownAsync": """import { useState, useRef, useEffect } from 'react'

export default function AsyncDropdown({ label = 'Search...', fetchOptions }) {
  const [isOpen, setIsOpen] = useState(false)
  const [searchTerm, setSearchTerm] = useState('')
  const [options, setOptions] = useState([])
  const [loading, setLoading] = useState(false)
  const [selected, setSelected] = useState(null)
  const dropdownRef = useRef(null)

  useEffect(() => {
    const loadOptions = async () => {
      if (searchTerm.length < 2) {
        setOptions([])
        return
      }

      setLoading(true)
      try {
        const results = await fetchOptions(searchTerm)
        setOptions(results)
      } catch (error) {
        console.error('Failed to fetch options:', error)
      }
      setLoading(false)
    }

    const debounceTimer = setTimeout(loadOptions, 300)
    return () => clearTimeout(debounceTimer)
  }, [searchTerm, fetchOptions])

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  return (
    <div className="async-dropdown" ref={dropdownRef}>
      <input
        type="text"
        placeholder={selected ? selected.label : label}
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        onFocus={() => setIsOpen(true)}
      />
      {isOpen && (
        <div className="dropdown-menu">
          {loading && <div className="dropdown-item">Loading...</div>}
          {!loading && options.length === 0 && searchTerm.length >= 2 && (
            <div className="dropdown-item">No results found</div>
          )}
          {!loading && options.map((option) => (
            <button
              key={option.value}
              className="dropdown-item"
              onClick={() => {
                setSelected(option)
                setSearchTerm('')
                setIsOpen(false)
              }}
            >
              {option.label}
            </button>
          ))}
        </div>
      )}
    </div>
  )
}""",

    "DropdownCascading": """import { useState, useRef, useEffect } from 'react'

export default function CascadingDropdown({ levels = [] }) {
  const [selectedPath, setSelectedPath] = useState([])
  const [isOpen, setIsOpen] = useState(false)
  const dropdownRef = useRef(null)

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  const handleSelect = (levelIndex, option) => {
    const newPath = [...selectedPath.slice(0, levelIndex), option]
    setSelectedPath(newPath)

    if (!option.children || option.children.length === 0) {
      setIsOpen(false)
    }
  }

  const getOptions = (levelIndex) => {
    if (levelIndex === 0) return levels[0].options
    const parent = selectedPath[levelIndex - 1]
    return parent?.children || []
  }

  return (
    <div className="cascading-dropdown" ref={dropdownRef}>
      <button className="dropdown-trigger" onClick={() => setIsOpen(!isOpen)}>
        {selectedPath.length > 0 ? selectedPath.map(s => s.label).join(' > ') : 'Select...'}
      </button>
      {isOpen && (
        <div className="dropdown-menu cascading">
          {levels.map((level, levelIndex) => {
            const options = getOptions(levelIndex)
            if (!options || options.length === 0) return null

            return (
              <div key={levelIndex} className="dropdown-level">
                <div className="level-title">{level.label}</div>
                {options.map((option) => (
                  <button
                    key={option.value}
                    className={`dropdown-item ${selectedPath[levelIndex]?.value === option.value ? 'selected' : ''}`}
                    onClick={() => handleSelect(levelIndex, option)}
                  >
                    {option.label}
                    {option.children && option.children.length > 0 && <span> ›</span>}
                  </button>
                ))}
              </div>
            )
          })}
        </div>
      )}
    </div>
  )
}""",

    "DropdownTags": """import { useState, useRef, useEffect } from 'react'

export default function TagsDropdown({ options = [], placeholder = 'Add tags...' }) {
  const [isOpen, setIsOpen] = useState(false)
  const [searchTerm, setSearchTerm] = useState('')
  const [selected, setSelected] = useState([])
  const dropdownRef = useRef(null)
  const inputRef = useRef(null)

  const filteredOptions = options.filter(option =>
    !selected.find(s => s.value === option.value) &&
    option.label.toLowerCase().includes(searchTerm.toLowerCase())
  )

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  const addTag = (option) => {
    setSelected([...selected, option])
    setSearchTerm('')
    inputRef.current?.focus()
  }

  const removeTag = (option) => {
    setSelected(selected.filter(s => s.value !== option.value))
  }

  return (
    <div className="tags-dropdown" ref={dropdownRef}>
      <div className="tags-input-container">
        {selected.map((tag) => (
          <span key={tag.value} className="tag">
            {tag.label}
            <button onClick={() => removeTag(tag)}>×</button>
          </span>
        ))}
        <input
          ref={inputRef}
          type="text"
          placeholder={selected.length === 0 ? placeholder : ''}
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          onFocus={() => setIsOpen(true)}
        />
      </div>
      {isOpen && filteredOptions.length > 0 && (
        <div className="dropdown-menu">
          {filteredOptions.map((option) => (
            <button
              key={option.value}
              className="dropdown-item"
              onClick={() => addTag(option)}
            >
              {option.label}
            </button>
          ))}
        </div>
      )}
    </div>
  )
}""",

    "DropdownAutocomplete": """import { useState, useRef, useEffect } from 'react'

export default function Autocomplete({ options = [], placeholder = 'Type to search...' }) {
  const [isOpen, setIsOpen] = useState(false)
  const [inputValue, setInputValue] = useState('')
  const [highlightedIndex, setHighlightedIndex] = useState(0)
  const dropdownRef = useRef(null)

  const filteredOptions = options.filter(option =>
    option.label.toLowerCase().includes(inputValue.toLowerCase())
  )

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  const handleKeyDown = (e) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault()
      setHighlightedIndex((prev) => Math.min(prev + 1, filteredOptions.length - 1))
    } else if (e.key === 'ArrowUp') {
      e.preventDefault()
      setHighlightedIndex((prev) => Math.max(prev - 1, 0))
    } else if (e.key === 'Enter') {
      e.preventDefault()
      if (filteredOptions[highlightedIndex]) {
        setInputValue(filteredOptions[highlightedIndex].label)
        setIsOpen(false)
      }
    }
  }

  return (
    <div className="autocomplete" ref={dropdownRef}>
      <input
        type="text"
        placeholder={placeholder}
        value={inputValue}
        onChange={(e) => {
          setInputValue(e.target.value)
          setIsOpen(true)
          setHighlightedIndex(0)
        }}
        onKeyDown={handleKeyDown}
        onFocus={() => setIsOpen(true)}
      />
      {isOpen && filteredOptions.length > 0 && (
        <div className="dropdown-menu">
          {filteredOptions.map((option, index) => (
            <button
              key={option.value}
              className={`dropdown-item ${index === highlightedIndex ? 'highlighted' : ''}`}
              onClick={() => {
                setInputValue(option.label)
                setIsOpen(false)
              }}
              onMouseEnter={() => setHighlightedIndex(index)}
            >
              {option.label}
            </button>
          ))}
        </div>
      )}
    </div>
  )
}"""
}

def write_components():
    """Write all components to files"""

    # Write accordions
    accordion_dir = COMPONENTS_DIR / "accordions"
    for name, code in accordions.items():
        (accordion_dir / f"{name}.jsx").write_text(code, encoding='utf-8')
    print(f"✓ Generated {len(accordions)} accordion components")

    # Write carousels
    carousel_dir = COMPONENTS_DIR / "carousels"
    for name, code in carousels.items():
        (carousel_dir / f"{name}.jsx").write_text(code, encoding='utf-8')
    print(f"✓ Generated {len(carousels)} carousel components")

    # Write dropdowns
    dropdown_dir = COMPONENTS_DIR / "dropdowns"
    for name, code in dropdowns.items():
        (dropdown_dir / f"{name}.jsx").write_text(code, encoding='utf-8')
    print(f"✓ Generated {len(dropdowns)} dropdown components")

if __name__ == "__main__":
    write_components()
    print(f"\n✅ Total Advanced UI Components: {len(accordions) + len(carousels) + len(dropdowns)}")
