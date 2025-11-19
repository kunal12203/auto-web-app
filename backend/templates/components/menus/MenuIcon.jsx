export default function IconMenu({ items = [] }) {
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
}