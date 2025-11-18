export default function DashboardPreview() {
  return (
    <section className="dashboard-preview">
      <div className="container">
        <h2>{{DASHBOARD_HEADLINE}}</h2>
        <p>{{DASHBOARD_SUBHEADLINE}}</p>
        <div className="dashboard-mockup">
          <div className="dashboard-placeholder">
            📊 Dashboard Preview
          </div>
        </div>
      </div>
    </section>
  )
}