import { useState } from 'react'

/**
 * PickerDateRange
 * Description: date range picker
 */
export default function PickerDateRange({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="pickerdaterange" {...props}>
      <div className="pickerdaterange-content">
        {children}
      </div>
    </div>
  )
}