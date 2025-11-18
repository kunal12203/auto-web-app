import { useState } from 'react'

/**
 * TabsRouter
 * Description: router-integrated tabs
 */
export default function TabsRouter({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="tabsrouter" {...props}>
      <div className="tabsrouter-content">
        {children}
      </div>
    </div>
  )
}