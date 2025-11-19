export default function ChefProfile() {
  return (
    <section className="chef-profile">
      <div className="container">
        <div className="chef-grid">
          <div className="chef-image">{{CHEF_ICON}}</div>
          <div className="chef-info">
            <h2>{{CHEF_NAME}}</h2>
            <h3>{{CHEF_TITLE}}</h3>
            <p>{{CHEF_BIO}}</p>
          </div>
        </div>
      </div>
    </section>
  )
}