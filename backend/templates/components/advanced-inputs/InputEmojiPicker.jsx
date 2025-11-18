import { useState } from 'react'

/**
 * InputEmojiPicker
 * Description: emoji picker input
 */
export default function InputEmojiPicker({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputemojipicker" {...props}>
      <div className="inputemojipicker-content">
        {children}
      </div>
    </div>
  )
}