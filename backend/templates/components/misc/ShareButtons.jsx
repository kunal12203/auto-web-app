export default function ShareButtons() {
  const url = window.location.href

  return (
    <div className="share-buttons">
      <button onClick={() => window.open(`https://facebook.com/sharer/sharer.php?u=${url}`)}>
        Share on Facebook
      </button>
      <button onClick={() => window.open(`https://twitter.com/intent/tweet?url=${url}`)}>
        Share on Twitter
      </button>
    </div>
  )
}