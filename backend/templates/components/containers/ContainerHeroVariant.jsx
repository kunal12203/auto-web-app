import { useState } from 'react'

/**
 * ContainerHeroVariant
 * Description: hero container
 */
export default function ContainerHeroVariant({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="containerherovariant" {...props}>
      <div className="containerherovariant-content">
        {children}
      </div>
    </div>
  )
}