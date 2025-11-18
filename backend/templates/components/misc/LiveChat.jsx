import { useState } from 'react'

export default function LiveChat() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <>
      <button className="chat-bubble" onClick={() => setIsOpen(!isOpen)}>
        💬
      </button>
      {isOpen && (
        <div className="chat-window">
          <div className="chat-header">
            <span>Live Chat</span>
            <button onClick={() => setIsOpen(false)}>×</button>
          </div>
          <div className="chat-messages">
            <p>How can we help you today?</p>
          </div>
          <input type="text" placeholder="Type a message..." />
        </div>
      )}
    </>
  )
}