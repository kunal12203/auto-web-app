import { useState } from 'react'

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
}