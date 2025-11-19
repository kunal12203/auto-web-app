import { useState } from 'react'

export default function ReservationForm() {
  const [formData, setFormData] = useState({
    name: '', date: '', time: '', guests: 2
  })

  return (
    <section className="reservation-form">
      <div className="container">
        <h2>Make a Reservation</h2>
        <form onSubmit={(e) => e.preventDefault()}>
          <input type="text" placeholder="Name" required />
          <input type="date" required />
          <input type="time" required />
          <select>
            <option>2 guests</option>
            <option>4 guests</option>
            <option>6 guests</option>
          </select>
          <button type="submit" className="btn-primary">Reserve Table</button>
        </form>
      </div>
    </section>
  )
}