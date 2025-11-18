import { useState } from 'react'

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
}