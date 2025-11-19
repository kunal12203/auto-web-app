import { useState } from 'react'

/**
 * InputOTP
 * Description: OTP verification input
 */
export default function InputOTP({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="inputotp" {...props}>
      <div className="inputotp-content">
        {children}
      </div>
    </div>
  )
}