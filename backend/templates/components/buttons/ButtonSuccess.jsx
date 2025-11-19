import { forwardRef } from 'react'

const ButtonSuccess = forwardRef(({ children, onClick, disabled = false, loading = false, ...props }, ref) => {
  return (
    <button
      ref={ref}
      onClick={onClick}
      disabled={disabled || loading}
      className="buttonsuccess"
      {...props}
    >
      {loading && <span className="btn-loader"></span>}
      {children}
    </button>
  )
})

ButtonSuccess.displayName = 'ButtonSuccess'

export default ButtonSuccess