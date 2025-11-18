import { useState } from 'react'

/**
 * DragDropCalendar
 * Description: draggable calendar events
 */
export default function DragDropCalendar({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="dragdropcalendar" {...props}>
      <div className="dragdropcalendar-content">
        {children}
      </div>
    </div>
  )
}