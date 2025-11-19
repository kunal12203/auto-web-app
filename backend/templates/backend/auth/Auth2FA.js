// Two-Factor Authentication
import speakeasy from 'speakeasy'
import QRCode from 'qrcode'

export const generate2FASecret = async (user) => {
  const secret = speakeasy.generateSecret({
    name: `App:${user.email}`
  })

  user.twoFactorSecret = secret.base32
  user.twoFactorEnabled = false
  await user.save()

  const qrCode = await QRCode.toDataURL(secret.otpauth_url)

  return {
    secret: secret.base32,
    qrCode
  }
}

export const verify2FAToken = (user, token) => {
  return speakeasy.totp.verify({
    secret: user.twoFactorSecret,
    encoding: 'base32',
    token,
    window: 2
  })
}

export const enable2FA = async (user, token) => {
  const isValid = verify2FAToken(user, token)

  if (!isValid) {
    throw new Error('Invalid 2FA token')
  }

  user.twoFactorEnabled = true
  await user.save()

  return user
}