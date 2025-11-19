import { useState } from 'react'

/**
 * PickerColor
 * Description: color picker
 */
export default function PickerColor({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="pickercolor" {...props}>
      <div className="pickercolor-content">
        {children}
      </div>
    </div>
  )
}