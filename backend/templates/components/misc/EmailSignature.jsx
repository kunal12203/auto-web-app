export default function EmailSignature() {
  return (
    <div className="email-signature">
      <strong>{{NAME}}</strong>
      <p>{{TITLE}}</p>
      <p>{{COMPANY}}</p>
      <p>{{EMAIL}} | {{PHONE}}</p>
    </div>
  )
}