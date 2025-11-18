import { useState } from 'react'

/**
 * PickerEmoji
 * Description: emoji picker
 */
export default function PickerEmoji({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="pickeremoji" {...props}>
      <div className="pickeremoji-content">
        {children}
      </div>
    </div>
  )
}