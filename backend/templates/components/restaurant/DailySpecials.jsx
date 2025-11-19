export default function DailySpecials() {
  const days = [
    { day: 'Monday', special: '{{MONDAY_SPECIAL}}' },
    { day: 'Tuesday', special: '{{TUESDAY_SPECIAL}}' },
    { day: 'Wednesday', special: '{{WEDNESDAY_SPECIAL}}' }
  ]

  return (
    <section className="daily-specials">
      <div className="container">
        <h2>Daily Specials</h2>
        <div className="specials-list">
          {days.map((item, i) => (
            <div key={i} className="special-item">
              <strong>{item.day}</strong>
              <p>{item.special}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}