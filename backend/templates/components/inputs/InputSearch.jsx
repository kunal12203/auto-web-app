import { useState } from 'react'

/**
 * InputSearch
 * Description: search input field
 */
export default function InputSearch({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputsearch" {...props}>
      <div className="inputsearch-content">
        {children}
      </div>
    </div>
  )
}