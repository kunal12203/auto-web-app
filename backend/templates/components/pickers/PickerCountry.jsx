import { useState } from 'react'

/**
 * PickerCountry
 * Description: country picker
 */
export default function PickerCountry({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="pickercountry" {...props}>
      <div className="pickercountry-content">
        {children}
      </div>
    </div>
  )
}