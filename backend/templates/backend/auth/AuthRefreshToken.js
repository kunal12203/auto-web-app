// Refresh Token
export const generateRefreshToken = (user) => {
  return jwt.sign(
    { userId: user.id, type: 'refresh' },
    process.env.REFRESH_TOKEN_SECRET,
    { expiresIn: '30d' }
  )
}

export const refreshAccessToken = async (req, res) => {
  const { refreshToken } = req.body

  try {
    const decoded = jwt.verify(refreshToken, process.env.REFRESH_TOKEN_SECRET)

    if (decoded.type !== 'refresh') {
      throw new Error('Invalid token type')
    }

    const user = await User.findById(decoded.userId)

    if (!user) {
      throw new Error('User not found')
    }

    const newAccessToken = generateToken(user)

    res.json({ accessToken: newAccessToken })
  } catch (error) {
    res.status(401).json({ message: 'Invalid refresh token' })
  }
}