import { useState } from 'react'

/**
 * MediaTranscript
 * Description: transcript sync player
 */
export default function MediaTranscript({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="mediatranscript" {...props}>
      <div className="mediatranscript-content">
        {children}
      </div>
    </div>
  )
}