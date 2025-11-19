import { useState, useEffect } from 'react'

export default function ResponsiveDrawer({ children }) {
  const [isOpen, setIsOpen] = useState(false)
  const [isMobile, setIsMobile] = useState(false)

  useEffect(() => {
    const checkMobile = () => {
      setIsMobile(window.innerWidth < 768)
    }
    checkMobile()
    window.addEventListener('resize', checkMobile)
    return () => window.removeEventListener('resize', checkMobile)
  }, [])

  return (
    <>
      {isMobile && isOpen && <div className="drawer-overlay" onClick={() => setIsOpen(false)} />}
      {isMobile && <button onClick={() => setIsOpen(!isOpen)}>☰</button>}
      <div className={`drawer ${isMobile ? (isOpen ? 'open' : '') : 'permanent'}`}>
        {isMobile && <button className="drawer-close" onClick={() => setIsOpen(false)}>×</button>}
        <div className="drawer-content">{children}</div>
      </div>
    </>
  )
}