import { useState } from 'react'

/**
 * NotificationSnackbar
 * Description: snackbar notification
 */
export default function NotificationSnackbar({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="notificationsnackbar" {...props}>
      <div className="notificationsnackbar-content">
        {children}
      </div>
    </div>
  )
}