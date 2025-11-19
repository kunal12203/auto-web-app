import { useState } from 'react'

/**
 * PickerImageCrop
 * Description: image cropper
 */
export default function PickerImageCrop({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="pickerimagecrop" {...props}>
      <div className="pickerimagecrop-content">
        {children}
      </div>
    </div>
  )
}