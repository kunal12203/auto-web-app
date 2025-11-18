import { useState } from 'react'

/**
 * PickerIcon
 * Description: icon picker
 */
export default function PickerIcon({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="pickericon" {...props}>
      <div className="pickericon-content">
        {children}
      </div>
    </div>
  )
}