import { forwardRef } from 'react'

const ButtonGhost = forwardRef(({ children, onClick, disabled = false, loading = false, ...props }, ref) => {
  return (
    <button
      ref={ref}
      onClick={onClick}
      disabled={disabled || loading}
      className="buttonghost"
      {...props}
    >
      {loading && <span className="btn-loader"></span>}
      {children}
    </button>
  )
})

ButtonGhost.displayName = 'ButtonGhost'

export default ButtonGhost