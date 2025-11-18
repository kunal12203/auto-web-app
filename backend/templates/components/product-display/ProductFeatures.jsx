import { useState } from 'react'

export default function ProductFeatures({ children, ...props }) {
  const [isActive, setIsActive] = useState(false)

  return (
    <div className="productfeatures" {...props}>
      {children}
    </div>
  )
}