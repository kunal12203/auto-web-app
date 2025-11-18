// GraphQL Context
export const createContext = async ({ req }) => {
  const token = req.headers.authorization?.replace('Bearer ', '')

  let user = null
  if (token) {
    try {
      const decoded = verifyToken(token)
      user = await User.findById(decoded.userId)
    } catch (error) {
      // Invalid token
    }
  }

  return {
    user,
    models: {
      User,
      Post,
      Comment
    },
    loaders: createLoaders()
  }
}