import { useState } from 'react'

/**
 * MapLocationPicker
 * Description: location picker
 */
export default function MapLocationPicker({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="maplocationpicker" {...props}>
      <div className="maplocationpicker-content">
        {children}
      </div>
    </div>
  )
}