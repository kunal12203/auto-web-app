import { useState } from 'react'

/**
 * PickerFile
 * Description: file picker
 */
export default function PickerFile({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="pickerfile" {...props}>
      <div className="pickerfile-content">
        {children}
      </div>
    </div>
  )
}