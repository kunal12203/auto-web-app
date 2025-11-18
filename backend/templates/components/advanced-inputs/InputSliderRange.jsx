import { useState } from 'react'

/**
 * InputSliderRange
 * Description: range slider input
 */
export default function InputSliderRange({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputsliderrange" {...props}>
      <div className="inputsliderrange-content">
        {children}
      </div>
    </div>
  )
}