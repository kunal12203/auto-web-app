import { useState } from 'react'

/**
 * PickerTimezone
 * Description: timezone picker
 */
export default function PickerTimezone({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="pickertimezone" {...props}>
      <div className="pickertimezone-content">
        {children}
      </div>
    </div>
  )
}