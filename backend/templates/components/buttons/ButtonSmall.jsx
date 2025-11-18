import { forwardRef } from 'react'

const ButtonSmall = forwardRef(({ children, onClick, disabled = false, loading = false, ...props }, ref) => {
  return (
    <button
      ref={ref}
      onClick={onClick}
      disabled={disabled || loading}
      className="buttonsmall"
      {...props}
    >
      {loading && <span className="btn-loader"></span>}
      {children}
    </button>
  )
})

ButtonSmall.displayName = 'ButtonSmall'

export default ButtonSmall