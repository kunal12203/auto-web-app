export default function RichTooltip({ children, title, content, footer }) {
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
}