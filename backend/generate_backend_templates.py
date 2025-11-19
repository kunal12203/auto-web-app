"""
Generate 150-200 Backend Templates
- API routes, authentication, database operations, middleware, integrations, etc.
"""
from pathlib import Path

BACKEND_DIR = Path("templates/backend")

def write_template(category, name, code):
    category_dir = BACKEND_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)
    ext = ".js" if category not in ["docs"] else ".md"
    (category_dir / f"{name}{ext}").write_text(code, encoding='utf-8')

# API Templates
api_templates = {
    # REST API CRUD Operations (15)
    "RESTGetAll": """// GET all resources
export const getAll = async (req, res) => {
  try {
    const { page = 1, limit = 10, sort = 'createdAt', order = 'desc' } = req.query

    const resources = await Model.find()
      .sort({ [sort]: order === 'desc' ? -1 : 1 })
      .limit(limit * 1)
      .skip((page - 1) * limit)
      .exec()

    const count = await Model.countDocuments()

    res.json({
      resources,
      totalPages: Math.ceil(count / limit),
      currentPage: page,
      total: count
    })
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}""",

    "RESTGetById": """// GET single resource by ID
export const getById = async (req, res) => {
  try {
    const resource = await Model.findById(req.params.id)

    if (!resource) {
      return res.status(404).json({ message: 'Resource not found' })
    }

    res.json(resource)
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}""",

    "RESTCreate": """// POST create new resource
export const create = async (req, res) => {
  try {
    const resource = new Model(req.body)
    const savedResource = await resource.save()

    res.status(201).json(savedResource)
  } catch (error) {
    res.status(400).json({ message: error.message })
  }
}""",

    "RESTUpdate": """// PUT/PATCH update resource
export const update = async (req, res) => {
  try {
    const resource = await Model.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true, runValidators: true }
    )

    if (!resource) {
      return res.status(404).json({ message: 'Resource not found' })
    }

    res.json(resource)
  } catch (error) {
    res.status(400).json({ message: error.message })
  }
}""",

    "RESTDelete": """// DELETE resource
export const deleteResource = async (req, res) => {
  try {
    const resource = await Model.findByIdAndDelete(req.params.id)

    if (!resource) {
      return res.status(404).json({ message: 'Resource not found' })
    }

    res.json({ message: 'Resource deleted successfully' })
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}""",

    "RESTPagination": """// Pagination helper
export const paginate = async (req, res, Model) => {
  const page = parseInt(req.query.page) || 1
  const limit = parseInt(req.query.limit) || 10
  const skip = (page - 1) * limit

  const [results, total] = await Promise.all([
    Model.find().skip(skip).limit(limit),
    Model.countDocuments()
  ])

  return {
    results,
    pagination: {
      page,
      limit,
      total,
      pages: Math.ceil(total / limit),
      hasNext: page < Math.ceil(total / limit),
      hasPrev: page > 1
    }
  }
}""",

    "RESTSearch": """// Advanced search
export const search = async (req, res) => {
  try {
    const { q, fields = 'name,description' } = req.query

    const searchFields = fields.split(',')
    const searchQuery = {
      $or: searchFields.map(field => ({
        [field]: { $regex: q, $options: 'i' }
      }))
    }

    const results = await Model.find(searchQuery)

    res.json(results)
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}""",

    "RESTBulkCreate": """// Bulk create resources
export const bulkCreate = async (req, res) => {
  try {
    const resources = await Model.insertMany(req.body, { ordered: false })

    res.status(201).json({
      created: resources.length,
      resources
    })
  } catch (error) {
    res.status(400).json({ message: error.message })
  }
}""",

    "RESTBulkUpdate": """// Bulk update resources
export const bulkUpdate = async (req, res) => {
  try {
    const { ids, updates } = req.body

    const result = await Model.updateMany(
      { _id: { $in: ids } },
      updates
    )

    res.json({
      matched: result.matchedCount,
      modified: result.modifiedCount
    })
  } catch (error) {
    res.status(400).json({ message: error.message })
  }
}""",

    "RESTBulkDelete": """// Bulk delete resources
export const bulkDelete = async (req, res) => {
  try {
    const { ids } = req.body

    const result = await Model.deleteMany({ _id: { $in: ids } })

    res.json({
      deleted: result.deletedCount
    })
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}""",

    "RESTExport": """// Export data to CSV
export const exportCSV = async (req, res) => {
  try {
    const resources = await Model.find()

    const csv = resources.map(r => Object.values(r.toObject()).join(',')).join('\\n')
    const header = Object.keys(resources[0].toObject()).join(',')

    res.setHeader('Content-Type', 'text/csv')
    res.setHeader('Content-Disposition', 'attachment; filename=export.csv')
    res.send(header + '\\n' + csv)
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}""",

    "RESTImport": """// Import data from CSV
export const importCSV = async (req, res) => {
  try {
    const file = req.file
    const data = parseCSV(file.buffer)

    const resources = await Model.insertMany(data)

    res.json({
      imported: resources.length,
      resources
    })
  } catch (error) {
    res.status(400).json({ message: error.message })
  }
}""",

    "RESTSoftDelete": """// Soft delete resource
export const softDelete = async (req, res) => {
  try {
    const resource = await Model.findByIdAndUpdate(
      req.params.id,
      { deletedAt: new Date(), isDeleted: true },
      { new: true }
    )

    if (!resource) {
      return res.status(404).json({ message: 'Resource not found' })
    }

    res.json({ message: 'Resource soft deleted' })
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}""",

    "RESTRestore": """// Restore soft deleted resource
export const restore = async (req, res) => {
  try {
    const resource = await Model.findByIdAndUpdate(
      req.params.id,
      { deletedAt: null, isDeleted: false },
      { new: true }
    )

    if (!resource) {
      return res.status(404).json({ message: 'Resource not found' })
    }

    res.json({ message: 'Resource restored', resource })
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}""",

    "APIRateLimiting": """// Rate limiting middleware
import rateLimit from 'express-rate-limit'

export const rateLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP, please try again later.',
  standardHeaders: true,
  legacyHeaders: false,
})"""
}

# GraphQL Templates (10)
graphql_templates = {
    "GraphQLQueryResolver": """// GraphQL Query Resolver
export const Query = {
  getResource: async (_, { id }, context) => {
    return await context.models.Resource.findById(id)
  },

  listResources: async (_, { filter, pagination }, context) => {
    const resources = await context.models.Resource.find(filter)
      .limit(pagination.limit)
      .skip(pagination.offset)

    const total = await context.models.Resource.countDocuments(filter)

    return {
      resources,
      total,
      hasMore: pagination.offset + pagination.limit < total
    }
  }
}""",

    "GraphQLMutationResolver": """// GraphQL Mutation Resolver
export const Mutation = {
  createResource: async (_, { input }, context) => {
    const resource = new context.models.Resource(input)
    await resource.save()
    return resource
  },

  updateResource: async (_, { id, input }, context) => {
    const resource = await context.models.Resource.findByIdAndUpdate(
      id,
      input,
      { new: true, runValidators: true }
    )

    if (!resource) {
      throw new Error('Resource not found')
    }

    return resource
  },

  deleteResource: async (_, { id }, context) => {
    const resource = await context.models.Resource.findByIdAndDelete(id)

    if (!resource) {
      throw new Error('Resource not found')
    }

    return { success: true, message: 'Resource deleted' }
  }
}""",

    "GraphQLSubscription": """// GraphQL Subscription
import { PubSub } from 'graphql-subscriptions'

const pubsub = new PubSub()

export const Subscription = {
  resourceUpdated: {
    subscribe: () => pubsub.asyncIterator(['RESOURCE_UPDATED'])
  }
}

// Publish update
export const publishResourceUpdate = (resource) => {
  pubsub.publish('RESOURCE_UPDATED', {
    resourceUpdated: resource
  })
}""",

    "GraphQLDataLoader": """// DataLoader for N+1 prevention
import DataLoader from 'dataloader'

export const createLoaders = () => {
  return {
    userLoader: new DataLoader(async (ids) => {
      const users = await User.find({ _id: { $in: ids } })
      return ids.map(id => users.find(user => user.id === id))
    }),

    postLoader: new DataLoader(async (ids) => {
      const posts = await Post.find({ _id: { $in: ids } })
      return ids.map(id => posts.find(post => post.id === id))
    })
  }
}""",

    "GraphQLSchemaStitching": """// Schema Stitching
import { stitchSchemas } from '@graphql-tools/stitch'

export const stitchedSchema = stitchSchemas({
  subschemas: [
    {
      schema: userSchema,
      executor: userExecutor
    },
    {
      schema: productSchema,
      executor: productExecutor
    }
  ]
})""",

    "GraphQLFederation": """// Apollo Federation
import { buildFederatedSchema } from '@apollo/federation'

export const schema = buildFederatedSchema([
  {
    typeDefs,
    resolvers: {
      Query: {
        _entities(_, { representations }) {
          return representations.map((ref) => {
            if (ref.__typename === 'Product') {
              return getProduct(ref.id)
            }
          })
        }
      }
    }
  }
])""",

    "GraphQLDirective": """// Custom GraphQL Directive
import { SchemaDirectiveVisitor } from 'graphql-tools'

export class AuthDirective extends SchemaDirectiveVisitor {
  visitFieldDefinition(field) {
    const { resolve = defaultFieldResolver } = field
    const { role } = this.args

    field.resolve = async function (...args) {
      const context = args[2]

      if (!context.user) {
        throw new Error('Not authenticated')
      }

      if (role && !context.user.roles.includes(role)) {
        throw new Error('Not authorized')
      }

      return resolve.apply(this, args)
    }
  }
}""",

    "GraphQLScalar": """// Custom Scalar Type
import { GraphQLScalarType, Kind } from 'graphql'

export const DateTimeScalar = new GraphQLScalarType({
  name: 'DateTime',
  description: 'DateTime custom scalar type',

  serialize(value) {
    return value.toISOString()
  },

  parseValue(value) {
    return new Date(value)
  },

  parseLiteral(ast) {
    if (ast.kind === Kind.STRING) {
      return new Date(ast.value)
    }
    return null
  }
})""",

    "GraphQLErrorHandling": """// GraphQL Error Handling
import { ApolloError } from 'apollo-server-express'

export class NotFoundError extends ApolloError {
  constructor(message) {
    super(message, 'NOT_FOUND')
  }
}

export class ValidationError extends ApolloError {
  constructor(message, validationErrors) {
    super(message, 'VALIDATION_ERROR', { validationErrors })
  }
}

export const formatError = (error) => {
  // Log errors
  console.error(error)

  // Don't expose internal errors to client
  if (error.message.startsWith('Database')) {
    return new Error('Internal server error')
  }

  return error
}""",

    "GraphQLContext": """// GraphQL Context
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
}"""
}

# Authentication Templates (12)
auth_templates = {
    "AuthJWT": """// JWT Authentication
import jwt from 'jsonwebtoken'

export const generateToken = (user) => {
  return jwt.sign(
    { userId: user.id, email: user.email },
    process.env.JWT_SECRET,
    { expiresIn: '7d' }
  )
}

export const verifyToken = (token) => {
  try {
    return jwt.verify(token, process.env.JWT_SECRET)
  } catch (error) {
    throw new Error('Invalid token')
  }
}""",

    "AuthOAuth2": """// OAuth2 Authentication
import passport from 'passport'
import { Strategy as GoogleStrategy } from 'passport-google-oauth20'

passport.use(new GoogleStrategy({
    clientID: process.env.GOOGLE_CLIENT_ID,
    clientSecret: process.env.GOOGLE_CLIENT_SECRET,
    callbackURL: '/auth/google/callback'
  },
  async (accessToken, refreshToken, profile, done) => {
    try {
      let user = await User.findOne({ googleId: profile.id })

      if (!user) {
        user = await User.create({
          googleId: profile.id,
          email: profile.emails[0].value,
          name: profile.displayName
        })
      }

      return done(null, user)
    } catch (error) {
      return done(error, null)
    }
  }
))

export const googleAuth = passport.authenticate('google', {
  scope: ['profile', 'email']
})

export const googleCallback = passport.authenticate('google', {
  failureRedirect: '/login'
})""",

    "AuthSessionBased": """// Session-based Authentication
import session from 'express-session'
import MongoStore from 'connect-mongo'

export const sessionMiddleware = session({
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false,
  store: MongoStore.create({
    mongoUrl: process.env.MONGODB_URI,
    ttl: 24 * 60 * 60 // 1 day
  }),
  cookie: {
    maxAge: 24 * 60 * 60 * 1000,
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'strict'
  }
})""",

    "AuthRefreshToken": """// Refresh Token
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
}""",

    "AuthPasswordHash": """// Password Hashing
import bcrypt from 'bcryptjs'

export const hashPassword = async (password) => {
  const salt = await bcrypt.genSalt(10)
  return await bcrypt.hash(password, salt)
}

export const comparePassword = async (password, hash) => {
  return await bcrypt.compare(password, hash)
}""",

    "AuthPasswordReset": """// Password Reset
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
}""",

    "AuthEmailVerification": """// Email Verification
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
}""",

    "Auth2FA": """// Two-Factor Authentication
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
}""",

    "AuthSSO": """// Single Sign-On
import saml from 'passport-saml'

export const samlStrategy = new saml.Strategy({
    entryPoint: process.env.SAML_ENTRY_POINT,
    issuer: process.env.SAML_ISSUER,
    callbackUrl: process.env.SAML_CALLBACK_URL,
    cert: process.env.SAML_CERT
  },
  async (profile, done) => {
    try {
      let user = await User.findOne({ email: profile.email })

      if (!user) {
        user = await User.create({
          email: profile.email,
          name: profile.displayName,
          ssoId: profile.nameID
        })
      }

      return done(null, user)
    } catch (error) {
      return done(error, null)
    }
  }
)""",

    "AuthSocialLogin": """// Social Login Handler
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
}""",

    "AuthMagicLink": """// Magic Link Authentication
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
}""",

    "AuthPasswordless": """// Passwordless Authentication
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
}"""
}

# Write all backend templates
total_count = 0

for name, code in api_templates.items():
    write_template("api", name, code)
    total_count += 1
print(f"✓ Generated {len(api_templates)} API templates")

for name, code in graphql_templates.items():
    write_template("api/graphql", name, code)
    total_count += 1
print(f"✓ Generated {len(graphql_templates)} GraphQL templates")

for name, code in auth_templates.items():
    write_template("auth", name, code)
    total_count += 1
print(f"✓ Generated {len(auth_templates)} authentication templates")

print(f"\n✅ Total backend templates generated so far: {total_count}")
print(f"   Continuing with more categories...")
