import { forwardRef } from 'react'

const ButtonLink = forwardRef(({ children, onClick, disabled = false, loading = false, ...props }, ref) => {
  return (
    <button
      ref={ref}
      onClick={onClick}
      disabled={disabled || loading}
      className="buttonlink"
      {...props}
    >
      {loading && <span className="btn-loader"></span>}
      {children}
    </button>
  )
})

ButtonLink.displayName = 'ButtonLink'

export default ButtonLink