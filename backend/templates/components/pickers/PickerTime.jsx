import { useState } from 'react'

/**
 * PickerTime
 * Description: time picker
 */
export default function PickerTime({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="pickertime" {...props}>
      <div className="pickertime-content">
        {children}
      </div>
    </div>
  )
}