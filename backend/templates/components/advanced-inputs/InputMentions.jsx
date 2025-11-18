import { useState } from 'react'

/**
 * InputMentions
 * Description: mentions/tagging input
 */
export default function InputMentions({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputmentions" {...props}>
      <div className="inputmentions-content">
        {children}
      </div>
    </div>
  )
}