import { useState } from 'react'

/**
 * PickerDate
 * Description: date picker
 */
export default function PickerDate({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="pickerdate" {...props}>
      <div className="pickerdate-content">
        {children}
      </div>
    </div>
  )
}