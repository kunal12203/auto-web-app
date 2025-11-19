import { useState } from 'react'

/**
 * InputRating
 * Description: star rating input
 */
export default function InputRating({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputrating" {...props}>
      <div className="inputrating-content">
        {children}
      </div>
    </div>
  )
}