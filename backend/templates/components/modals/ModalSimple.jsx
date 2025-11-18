import { useState } from 'react'

export default function ModalSimple() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <>
      <button onClick={() => setIsOpen(true)}>Open Modal</button>
      {isOpen && (
        <div className="modal-overlay" onClick={() => setIsOpen(false)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <button className="modal-close" onClick={() => setIsOpen(false)}>×</button>
            <h2>{{MODAL_TITLE}}</h2>
            <p>{{MODAL_CONTENT}}</p>
          </div>
        </div>
      )}
    </>
  )
}