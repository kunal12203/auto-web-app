export default function AlertError() {
  return (
    <div className="alert alert-error">
      <span>✗</span>
      <p>{{ERROR_MESSAGE}}</p>
    </div>
  )
}