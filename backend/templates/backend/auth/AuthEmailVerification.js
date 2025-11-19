// Email Verification
import crypto from 'crypto'

export const generateVerificationToken = async (user) => {
  const verificationToken = crypto.randomBytes(32).toString('hex')

  user.verificationToken = crypto
    .createHash('sha256')
    .update(verificationToken)
    .digest('hex')

  await user.save()

  return verificationToken
}

export const verifyEmail = async (token) => {
  const hashedToken = crypto
    .createHash('sha256')
    .update(token)
    .digest('hex')

  const user = await User.findOne({
    verificationToken: hashedToken
  })

  if (!user) {
    throw new Error('Invalid verification token')
  }

  user.isVerified = true
  user.verificationToken = undefined

  await user.save()

  return user
}