import { forwardRef } from 'react'

const ButtonShadow = forwardRef(({ children, onClick, disabled = false, loading = false, ...props }, ref) => {
  return (
    <button
      ref={ref}
      onClick={onClick}
      disabled={disabled || loading}
      className="buttonshadow"
      {...props}
    >
      {loading && <span className="btn-loader"></span>}
      {children}
    </button>
  )
})

ButtonShadow.displayName = 'ButtonShadow'

export default ButtonShadow