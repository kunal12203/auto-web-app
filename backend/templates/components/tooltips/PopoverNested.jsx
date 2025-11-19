import { useState } from 'react'

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
}