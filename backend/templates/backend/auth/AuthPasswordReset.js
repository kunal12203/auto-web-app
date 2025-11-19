// Password Reset
import crypto from 'crypto'

export const generateResetToken = async (user) => {
  const resetToken = crypto.randomBytes(32).toString('hex')

  user.resetPasswordToken = crypto
    .createHash('sha256')
    .update(resetToken)
    .digest('hex')

  user.resetPasswordExpires = Date.now() + 10 * 60 * 1000 // 10 minutes

  await user.save()

  return resetToken
}

export const resetPassword = async (token, newPassword) => {
  const hashedToken = crypto
    .createHash('sha256')
    .update(token)
    .digest('hex')

  const user = await User.findOne({
    resetPasswordToken: hashedToken,
    resetPasswordExpires: { $gt: Date.now() }
  })

  if (!user) {
    throw new Error('Invalid or expired reset token')
  }

  user.password = await hashPassword(newPassword)
  user.resetPasswordToken = undefined
  user.resetPasswordExpires = undefined

  await user.save()

  return user
}