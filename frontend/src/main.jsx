import React from 'react'
import ReactDOM from 'react-dom/client'
import ChatApp from './ChatApp' // ChatApp has thread management and full features
import './index.css' // Global resets

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ChatApp />
  </React.StrictMode>,
)