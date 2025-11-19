import { useState } from 'react'

export default function Sidebar() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <>
      <button onClick={() => setIsOpen(!isOpen)} className="sidebar-toggle">
        Menu
      </button>
      <aside className={`sidebar ${isOpen ? 'open' : ''}`}>
        <nav>
          <a href="#dashboard">Dashboard</a>
          <a href="#projects">Projects</a>
          <a href="#team">Team</a>
          <a href="#settings">Settings</a>
        </nav>
      </aside>
    </>
  )
}