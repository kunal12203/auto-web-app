import { useState } from 'react'

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
}