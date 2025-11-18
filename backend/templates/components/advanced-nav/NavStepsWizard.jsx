import { useState } from 'react'

/**
 * NavStepsWizard
 * Description: step wizard navigation
 */
export default function NavStepsWizard({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="navstepswizard" {...props}>
      <div className="navstepswizard-content">
        {children}
      </div>
    </div>
  )
}