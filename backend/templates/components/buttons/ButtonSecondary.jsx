import { forwardRef } from 'react'

const ButtonSecondary = forwardRef(({ children, onClick, disabled = false, loading = false, ...props }, ref) => {
  return (
    <button
      ref={ref}
      onClick={onClick}
      disabled={disabled || loading}
      className="buttonsecondary"
      {...props}
    >
      {loading && <span className="btn-loader"></span>}
      {children}
    </button>
  )
})

ButtonSecondary.displayName = 'ButtonSecondary'

export default ButtonSecondary