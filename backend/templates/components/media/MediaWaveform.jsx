import { useState } from 'react'

/**
 * MediaWaveform
 * Description: audio waveform
 */
export default function MediaWaveform({ children, ...props }) {
  const [state, setState] = useState(null)

  return (
    <div className="mediawaveform" {...props}>
      <div className="mediawaveform-content">
        {children}
      </div>
    </div>
  )
}