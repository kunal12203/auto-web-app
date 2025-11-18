export default function SocialShare() {
  const shareUrl = window.location.href

  return (
    <div className="social-share">
      <p>Share this:</p>
      <button onClick={() => window.open(`https://facebook.com/sharer/sharer.php?u=${shareUrl}`)}>
        Facebook
      </button>
      <button onClick={() => window.open(`https://twitter.com/intent/tweet?url=${shareUrl}`)}>
        Twitter
      </button>
      <button onClick={() => window.open(`https://linkedin.com/sharing/share-offsite/?url=${shareUrl}`)}>
        LinkedIn
      </button>
    </div>
  )
}