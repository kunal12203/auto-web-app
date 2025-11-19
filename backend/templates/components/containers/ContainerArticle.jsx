import { useState } from 'react'

/**
 * ContainerArticle
 * Description: article container
 */
export default function ContainerArticle({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="containerarticle" {...props}>
      <div className="containerarticle-content">
        {children}
      </div>
    </div>
  )
}