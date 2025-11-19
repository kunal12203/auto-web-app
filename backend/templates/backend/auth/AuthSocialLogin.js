// Social Login Handler
export const socialLogin = async (provider, profile) => {
  let user = await User.findOne({ [`${provider}Id`]: profile.id })

  if (!user) {
    // Check if user exists with same email
    user = await User.findOne({ email: profile.email })

    if (user) {
      // Link social account to existing user
      user[`${provider}Id`] = profile.id
    } else {
      // Create new user
      user = new User({
        email: profile.email,
        name: profile.displayName,
        [`${provider}Id`]: profile.id,
        profilePicture: profile.photos[0]?.value,
        isVerified: true
      })
    }

    await user.save()
  }

  const token = generateToken(user)
  const refreshToken = generateRefreshToken(user)

  return { user, token, refreshToken }
}