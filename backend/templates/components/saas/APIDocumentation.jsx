export default function APIDocumentation() {
  const endpoints = [
    { method: 'GET', path: '/api/users', description: '{{API_1_DESC}}' },
    { method: 'POST', path: '/api/users', description: '{{API_2_DESC}}' },
    { method: 'PUT', path: '/api/users/:id', description: '{{API_3_DESC}}' }
  ]

  return (
    <section className="api-docs">
      <div className="container">
        <h2>API Documentation</h2>
        <div className="api-endpoints">
          {endpoints.map((endpoint, i) => (
            <div key={i} className="api-endpoint">
              <span className={`method method-${endpoint.method.toLowerCase()}`}>
                {endpoint.method}
              </span>
              <code>{endpoint.path}</code>
              <p>{endpoint.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}