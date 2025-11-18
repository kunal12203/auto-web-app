export default function Tooltip({ children, content, position = 'top' }) {
  return (
    <div className="tooltip-container">
      {children}
      <div className={`tooltip tooltip-${position}`}>{content}</div>
    </div>
  )
}