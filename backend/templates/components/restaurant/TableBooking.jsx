import { useState } from 'react'

export default function TableBooking() {
  return (
    <section className="table-booking">
      <div className="container">
        <h2>Book a Table</h2>
        <form onSubmit={(e) => e.preventDefault()} className="booking-form">
          <div className="form-row">
            <select>
              <option>2 people</option>
              <option>4 people</option>
              <option>6 people</option>
            </select>
            <input type="date" required />
            <input type="time" required />
          </div>
          <button type="submit" className="btn-primary">Book Now</button>
        </form>
      </div>
    </section>
  )
}