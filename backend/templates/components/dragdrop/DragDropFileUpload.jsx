import { useState } from 'react'

/**
 * DragDropFileUpload
 * Description: drag and drop file uploader
 */
export default function DragDropFileUpload({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="dragdropfileupload" {...props}>
      <div className="dragdropfileupload-content">
        {children}
      </div>
    </div>
  )
}