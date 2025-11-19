// Magic Link Authentication
import crypto from 'crypto'
import { sendEmail } from './email'

export const sendMagicLink = async (email) => {
  const user = await User.findOne({ email })

  if (!user) {
    // Don't reveal if user exists
    return { success: true }
  }

  const token = crypto.randomBytes(32).toString('hex')
  const hashedToken = crypto.createHash('sha256').update(token).digest('hex')

  user.magicLinkToken = hashedToken
  user.magicLinkExpires = Date.now() + 15 * 60 * 1000 // 15 minutes
  await user.save()

  const magicLink = `${process.env.APP_URL}/auth/magic-link/${token}`

  await sendEmail({
    to: email,
    subject: 'Your Magic Link',
    html: `<a href="${magicLink}">Click here to log in</a>`
  })

  return { success: true }
}

export const verifyMagicLink = async (token) => {
  const hashedToken = crypto.createHash('sha256').update(token).digest('hex')

  const user = await User.findOne({
    magicLinkToken: hashedToken,
    magicLinkExpires: { $gt: Date.now() }
  })

  if (!user) {
    throw new Error('Invalid or expired magic link')
  }

  user.magicLinkToken = undefined
  user.magicLinkExpires = undefined
  await user.save()

  const accessToken = generateToken(user)
  const refreshToken = generateRefreshToken(user)

  return { user, accessToken, refreshToken }
}