export default function StackedDialog({ dialogs = [], onCloseAll }) {
  return (
    <>
      {dialogs.length > 0 && <div className="dialog-overlay" onClick={onCloseAll} />}
      {dialogs.map((dialog, index) => (
        <div
          key={index}
          className="dialog"
          style={{
            zIndex: 1000 + index,
            transform: `scale(${1 - index * 0.05})`,
            opacity: 1 - index * 0.2
          }}
        >
          <div className="dialog-header">
            <h2>{dialog.title}</h2>
            <button onClick={() => dialog.onClose(index)}>×</button>
          </div>
          <div className="dialog-content">{dialog.content}</div>
        </div>
      ))}
    </>
  )
}