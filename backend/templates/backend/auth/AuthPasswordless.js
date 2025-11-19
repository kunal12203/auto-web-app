// Passwordless Authentication
import crypto from 'crypto'

export const requestPasswordlessAuth = async (email) => {
  const code = crypto.randomInt(100000, 999999).toString()

  await redis.setex(
    `auth:${email}`,
    300, // 5 minutes
    code
  )

  await sendEmail({
    to: email,
    subject: 'Your verification code',
    text: `Your verification code is: ${code}`
  })

  return { success: true }
}

export const verifyPasswordlessAuth = async (email, code) => {
  const storedCode = await redis.get(`auth:${email}`)

  if (!storedCode || storedCode !== code) {
    throw new Error('Invalid or expired code')
  }

  await redis.del(`auth:${email}`)

  let user = await User.findOne({ email })

  if (!user) {
    user = await User.create({
      email,
      isVerified: true
    })
  }

  const token = generateToken(user)
  const refreshToken = generateRefreshToken(user)

  return { user, token, refreshToken }
}