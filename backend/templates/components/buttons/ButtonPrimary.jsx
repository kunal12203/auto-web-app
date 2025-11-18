import { forwardRef } from 'react'

const ButtonPrimary = forwardRef(({ children, onClick, disabled = false, loading = false, ...props }, ref) => {
  return (
    <button
      ref={ref}
      onClick={onClick}
      disabled={disabled || loading}
      className="buttonprimary"
      {...props}
    >
      {loading && <span className="btn-loader"></span>}
      {children}
    </button>
  )
})

ButtonPrimary.displayName = 'ButtonPrimary'

export default ButtonPrimary