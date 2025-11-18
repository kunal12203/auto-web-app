import { useState } from 'react'

/**
 * InputFile
 * Description: file upload input
 */
export default function InputFile({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputfile" {...props}>
      <div className="inputfile-content">
        {children}
      </div>
    </div>
  )
}