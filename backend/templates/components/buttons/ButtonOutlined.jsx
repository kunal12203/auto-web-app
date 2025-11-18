import { forwardRef } from 'react'

const ButtonOutlined = forwardRef(({ children, onClick, disabled = false, loading = false, ...props }, ref) => {
  return (
    <button
      ref={ref}
      onClick={onClick}
      disabled={disabled || loading}
      className="buttonoutlined"
      {...props}
    >
      {loading && <span className="btn-loader"></span>}
      {children}
    </button>
  )
})

ButtonOutlined.displayName = 'ButtonOutlined'

export default ButtonOutlined