export default function ComingSoon() {
  return (
    <section className="coming-soon">
      <div className="container">
        <h1>Coming Soon</h1>
        <p>{{COMING_SOON_TEXT}}</p>
        <form onSubmit={(e) => e.preventDefault()}>
          <input type="email" placeholder="Get notified" />
          <button type="submit">Notify Me</button>
        </form>
      </div>
    </section>
  )
}