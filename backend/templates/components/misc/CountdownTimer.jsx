import { useState, useEffect } from 'react'

export default function CountdownTimer({ targetDate = '2024-12-31' }) {
  const [timeLeft, setTimeLeft] = useState({ days: 0, hours: 0, minutes: 0, seconds: 0 })

  useEffect(() => {
    const timer = setInterval(() => {
      const now = new Date().getTime()
      const target = new Date(targetDate).getTime()
      const distance = target - now

      setTimeLeft({
        days: Math.floor(distance / (1000 * 60 * 60 * 24)),
        hours: Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
        minutes: Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)),
        seconds: Math.floor((distance % (1000 * 60)) / 1000)
      })
    }, 1000)

    return () => clearInterval(timer)
  }, [targetDate])

  return (
    <div className="countdown-timer">
      <div className="countdown-item">
        <span>{timeLeft.days}</span>
        <span>Days</span>
      </div>
      <div className="countdown-item">
        <span>{timeLeft.hours}</span>
        <span>Hours</span>
      </div>
      <div className="countdown-item">
        <span>{timeLeft.minutes}</span>
        <span>Minutes</span>
      </div>
      <div className="countdown-item">
        <span>{timeLeft.seconds}</span>
        <span>Seconds</span>
      </div>
    </div>
  )
}