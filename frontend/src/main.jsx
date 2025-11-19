import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App' // Points to the modern conversational app
import './index.css' // Global resets

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)