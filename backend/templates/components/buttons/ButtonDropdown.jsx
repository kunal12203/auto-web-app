import { forwardRef } from 'react'

const ButtonDropdown = forwardRef(({ children, onClick, disabled = false, loading = false, ...props }, ref) => {
  return (
    <button
      ref={ref}
      onClick={onClick}
      disabled={disabled || loading}
      className="buttondropdown"
      {...props}
    >
      {loading && <span className="btn-loader"></span>}
      {children}
    </button>
  )
})

ButtonDropdown.displayName = 'ButtonDropdown'

export default ButtonDropdown