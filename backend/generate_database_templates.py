"""
Generate Database Templates (30-40)
- Schema definitions, migrations, seeders, connections for multiple databases
"""
from pathlib import Path

DATABASE_DIR = Path("templates/database")

def write_template(category, name, code):
    category_dir = DATABASE_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)
    (category_dir / f"{name}.js").write_text(code, encoding='utf-8')

# Schema Templates (15)
schemas = {
    "UserSchema": """import mongoose from 'mongoose'
import bcrypt from 'bcryptjs'

const userSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    trim: true
  },
  password: {
    type: String,
    required: true,
    minlength: 8
  },
  firstName: String,
  lastName: String,
  role: {
    type: String,
    enum: ['user', 'admin', 'moderator'],
    default: 'user'
  },
  isVerified: {
    type: Boolean,
    default: false
  },
  isActive: {
    type: Boolean,
    default: true
  }
}, {
  timestamps: true
})

userSchema.pre('save', async function(next) {
  if (!this.isModified('password')) return next()
  this.password = await bcrypt.hash(this.password, 10)
  next()
})

userSchema.methods.comparePassword = async function(candidatePassword) {
  return await bcrypt.compare(candidatePassword, this.password)
}

export const User = mongoose.model('User', userSchema)
""",

    "ProductSchema": """import mongoose from 'mongoose'

const productSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  slug: {
    type: String,
    required: true,
    unique: true
  },
  description: String,
  price: {
    type: Number,
    required: true,
    min: 0
  },
  compareAtPrice: Number,
  category: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Category'
  },
  images: [String],
  inventory: {
    quantity: {
      type: Number,
      default: 0
    },
    trackInventory: {
      type: Boolean,
      default: true
    }
  },
  isPublished: {
    type: Boolean,
    default: false
  },
  publishedAt: Date
}, {
  timestamps: true
})

productSchema.index({ name: 'text', description: 'text' })

export const Product = mongoose.model('Product', productSchema)
""",

    "OrderSchema": """import mongoose from 'mongoose'

const orderSchema = new mongoose.Schema({
  orderNumber: {
    type: String,
    required: true,
    unique: true
  },
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  items: [{
    product: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'Product'
    },
    quantity: {
      type: Number,
      required: true,
      min: 1
    },
    price: {
      type: Number,
      required: true
    }
  }],
  total: {
    type: Number,
    required: true
  },
  status: {
    type: String,
    enum: ['pending', 'processing', 'shipped', 'delivered', 'cancelled'],
    default: 'pending'
  },
  shippingAddress: {
    street: String,
    city: String,
    state: String,
    zipCode: String,
    country: String
  },
  payment: {
    method: String,
    transactionId: String,
    status: String
  }
}, {
  timestamps: true
})

export const Order = mongoose.model('Order', orderSchema)
""",

    "PostSchema": """import mongoose from 'mongoose'

const postSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true
  },
  slug: {
    type: String,
    required: true,
    unique: true
  },
  content: {
    type: String,
    required: true
  },
  excerpt: String,
  author: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  category: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Category'
  },
  tags: [{
    type: String
  }],
  featuredImage: String,
  status: {
    type: String,
    enum: ['draft', 'published', 'archived'],
    default: 'draft'
  },
  publishedAt: Date,
  viewCount: {
    type: Number,
    default: 0
  }
}, {
  timestamps: true
})

export const Post = mongoose.model('Post', postSchema)
""",

    "CommentSchema": """import mongoose from 'mongoose'

const commentSchema = new mongoose.Schema({
  content: {
    type: String,
    required: true
  },
  author: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  post: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Post',
    required: true
  },
  parent: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Comment'
  },
  isApproved: {
    type: Boolean,
    default: false
  },
  likes: {
    type: Number,
    default: 0
  }
}, {
  timestamps: true
})

export const Comment = mongoose.model('Comment', commentSchema)
""",

    "CategorySchema": """import mongoose from 'mongoose'

const categorySchema = new mongoose.Schema({
  name: {
    type: String,
    required: true
  },
  slug: {
    type: String,
    required: true,
    unique: true
  },
  description: String,
  parent: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Category'
  },
  icon: String,
  order: {
    type: Number,
    default: 0
  }
}, {
  timestamps: true
})

export const Category = mongoose.model('Category', categorySchema)
""",

    "RoleSchema": """import mongoose from 'mongoose'

const roleSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    unique: true
  },
  permissions: [{
    resource: String,
    actions: [String]
  }],
  description: String
}, {
  timestamps: true
})

export const Role = mongoose.model('Role', roleSchema)
""",

    "SessionSchema": """import mongoose from 'mongoose'

const sessionSchema = new mongoose.Schema({
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  token: {
    type: String,
    required: true,
    unique: true
  },
  ipAddress: String,
  userAgent: String,
  expiresAt: {
    type: Date,
    required: true
  },
  isActive: {
    type: Boolean,
    default: true
  }
}, {
  timestamps: true
})

sessionSchema.index({ expiresAt: 1 }, { expireAfterSeconds: 0 })

export const Session = mongoose.model('Session', sessionSchema)
""",

    "NotificationSchema": """import mongoose from 'mongoose'

const notificationSchema = new mongoose.Schema({
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  type: {
    type: String,
    required: true
  },
  title: String,
  message: {
    type: String,
    required: true
  },
  data: mongoose.Schema.Types.Mixed,
  isRead: {
    type: Boolean,
    default: false
  },
  readAt: Date
}, {
  timestamps: true
})

export const Notification = mongoose.model('Notification', notificationSchema)
""",

    "MediaSchema": """import mongoose from 'mongoose'

const mediaSchema = new mongoose.Schema({
  filename: {
    type: String,
    required: true
  },
  originalName: String,
  mimeType: String,
  size: Number,
  url: {
    type: String,
    required: true
  },
  thumbnailUrl: String,
  uploadedBy: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User'
  },
  folder: String,
  tags: [String],
  metadata: mongoose.Schema.Types.Mixed
}, {
  timestamps: true
})

export const Media = mongoose.model('Media', mediaSchema)
""",

    "CartSchema": """import mongoose from 'mongoose'

const cartSchema = new mongoose.Schema({
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User'
  },
  sessionId: String,
  items: [{
    product: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'Product'
    },
    quantity: {
      type: Number,
      min: 1,
      default: 1
    },
    price: Number
  }],
  total: Number,
  expiresAt: {
    type: Date,
    default: () => new Date(+new Date() + 7*24*60*60*1000)
  }
}, {
  timestamps: true
})

export const Cart = mongoose.model('Cart', cartSchema)
""",

    "ReviewSchema": """import mongoose from 'mongoose'

const reviewSchema = new mongoose.Schema({
  product: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Product',
    required: true
  },
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  rating: {
    type: Number,
    required: true,
    min: 1,
    max: 5
  },
  title: String,
  comment: String,
  isVerifiedPurchase: {
    type: Boolean,
    default: false
  },
  helpfulCount: {
    type: Number,
    default: 0
  }
}, {
  timestamps: true
})

export const Review = mongoose.model('Review', reviewSchema)
""",

    "SubscriptionSchema": """import mongoose from 'mongoose'

const subscriptionSchema = new mongoose.Schema({
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  plan: {
    type: String,
    required: true
  },
  status: {
    type: String,
    enum: ['active', 'cancelled', 'expired', 'past_due'],
    default: 'active'
  },
  startDate: {
    type: Date,
    required: true
  },
  endDate: Date,
  renewalDate: Date,
  paymentMethod: String,
  amount: Number
}, {
  timestamps: true
})

export const Subscription = mongoose.model('Subscription', subscriptionSchema)
""",

    "AuditLogSchema": """import mongoose from 'mongoose'

const auditLogSchema = new mongoose.Schema({
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User'
  },
  action: {
    type: String,
    required: true
  },
  resource: String,
  resourceId: mongoose.Schema.Types.ObjectId,
  changes: mongoose.Schema.Types.Mixed,
  ipAddress: String,
  userAgent: String,
  timestamp: {
    type: Date,
    default: Date.now
  }
}, {
  timestamps: false
})

export const AuditLog = mongoose.model('AuditLog', auditLogSchema)
""",

    "WebhookEventSchema": """import mongoose from 'mongoose'

const webhookEventSchema = new mongoose.Schema({
  type: {
    type: String,
    required: true
  },
  payload: {
    type: mongoose.Schema.Types.Mixed,
    required: true
  },
  source: String,
  processed: {
    type: Boolean,
    default: false
  },
  processedAt: Date,
  attempts: {
    type: Number,
    default: 0
  },
  lastError: String
}, {
  timestamps: true
})

export const WebhookEvent = mongoose.model('WebhookEvent', webhookEventSchema)
"""
}

# Migration Templates (8)
migrations = {
    "CreateUsersTable": """export const up = async (db) => {
  await db.createCollection('users', {
    validator: {
      $jsonSchema: {
        bsonType: 'object',
        required: ['email', 'password'],
        properties: {
          email: { bsonType: 'string' },
          password: { bsonType: 'string' },
          role: { enum: ['user', 'admin'] }
        }
      }
    }
  })

  await db.collection('users').createIndex({ email: 1 }, { unique: true })
}

export const down = async (db) => {
  await db.collection('users').drop()
}
""",

    "AddIndexes": """export const up = async (db) => {
  await db.collection('posts').createIndex({ slug: 1 }, { unique: true })
  await db.collection('posts').createIndex({ author: 1 })
  await db.collection('posts').createIndex({ publishedAt: -1 })
  await db.collection('posts').createIndex(
    { title: 'text', content: 'text' },
    { weights: { title: 10, content: 5 } }
  )
}

export const down = async (db) => {
  await db.collection('posts').dropIndex('slug_1')
  await db.collection('posts').dropIndex('author_1')
  await db.collection('posts').dropIndex('publishedAt_-1')
  await db.collection('posts').dropIndex('title_text_content_text')
}
""",

    "AddTimestamps": """export const up = async (db) => {
  const now = new Date()

  await db.collection('products').updateMany(
    {},
    {
      $set: {
        createdAt: now,
        updatedAt: now
      }
    }
  )
}

export const down = async (db) => {
  await db.collection('products').updateMany(
    {},
    {
      $unset: {
        createdAt: '',
        updatedAt: ''
      }
    }
  )
}
""",

    "AddForeignKey": """export const up = async (db) => {
  // Add foreign key constraint (MongoDB doesn't enforce, this is for documentation)
  await db.collection('posts').createIndex({ author: 1 })
  await db.collection('comments').createIndex({ post: 1 })
}

export const down = async (db) => {
  await db.collection('posts').dropIndex('author_1')
  await db.collection('comments').dropIndex('post_1')
}
""",

    "RenameField": """export const up = async (db) => {
  await db.collection('users').updateMany(
    {},
    {
      $rename: {
        'name': 'fullName'
      }
    }
  )
}

export const down = async (db) => {
  await db.collection('users').updateMany(
    {},
    {
      $rename: {
        'fullName': 'name'
      }
    }
  )
}
""",

    "AddNewField": """export const up = async (db) => {
  await db.collection('users').updateMany(
    {},
    {
      $set: {
        isActive: true
      }
    }
  )
}

export const down = async (db) => {
  await db.collection('users').updateMany(
    {},
    {
      $unset: {
        isActive: ''
      }
    }
  )
}
""",

    "ChangeDataType": """export const up = async (db) => {
  const users = await db.collection('users').find({}).toArray()

  for (const user of users) {
    await db.collection('users').updateOne(
      { _id: user._id },
      {
        $set: {
          age: parseInt(user.age)
        }
      }
    )
  }
}

export const down = async (db) => {
  const users = await db.collection('users').find({}).toArray()

  for (const user of users) {
    await db.collection('users').updateOne(
      { _id: user._id },
      {
        $set: {
          age: String(user.age)
        }
      }
    )
  }
}
""",

    "SeedInitialData": """export const up = async (db) => {
  const categories = [
    { name: 'Technology', slug: 'technology' },
    { name: 'Business', slug: 'business' },
    { name: 'Lifestyle', slug: 'lifestyle' }
  ]

  await db.collection('categories').insertMany(categories)
}

export const down = async (db) => {
  await db.collection('categories').deleteMany({
    slug: { $in: ['technology', 'business', 'lifestyle'] }
  })
}
"""
}

# Connection Templates (10)
connections = {
    "MongoDBConnection": """import mongoose from 'mongoose'

export const connectMongoDB = async () => {
  try {
    const options = {
      useNewUrlParser: true,
      useUnifiedTopology: true,
      maxPoolSize: 10,
      serverSelectionTimeoutMS: 5000,
      socketTimeoutMS: 45000,
    }

    await mongoose.connect(process.env.MONGODB_URI, options)

    console.log('MongoDB connected successfully')

    mongoose.connection.on('error', (error) => {
      console.error('MongoDB connection error:', error)
    })

    mongoose.connection.on('disconnected', () => {
      console.log('MongoDB disconnected')
    })

  } catch (error) {
    console.error('Failed to connect to MongoDB:', error)
    process.exit(1)
  }
}

export const disconnectMongoDB = async () => {
  await mongoose.connection.close()
}
""",

    "PostgreSQLConnection": """import { Pool } from 'pg'

const pool = new Pool({
  host: process.env.POSTGRES_HOST,
  port: process.env.POSTGRES_PORT,
  user: process.env.POSTGRES_USER,
  password: process.env.POSTGRES_PASSWORD,
  database: process.env.POSTGRES_DB,
  max: 20,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
})

pool.on('error', (err) => {
  console.error('Unexpected error on idle client', err)
  process.exit(-1)
})

export const query = (text, params) => pool.query(text, params)

export const getClient = () => pool.connect()

export default pool
""",

    "MySQLConnection": """import mysql from 'mysql2/promise'

const poolConfig = {
  host: process.env.MYSQL_HOST,
  user: process.env.MYSQL_USER,
  password: process.env.MYSQL_PASSWORD,
  database: process.env.MYSQL_DB,
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
}

export const pool = mysql.createPool(poolConfig)

export const query = async (sql, params) => {
  const [rows] = await pool.execute(sql, params)
  return rows
}

export const transaction = async (callback) => {
  const connection = await pool.getConnection()
  await connection.beginTransaction()

  try {
    await callback(connection)
    await connection.commit()
  } catch (error) {
    await connection.rollback()
    throw error
  } finally {
    connection.release()
  }
}
""",

    "RedisConnection": """import Redis from 'ioredis'

export const redis = new Redis({
  host: process.env.REDIS_HOST,
  port: process.env.REDIS_PORT,
  password: process.env.REDIS_PASSWORD,
  retryStrategy(times) {
    const delay = Math.min(times * 50, 2000)
    return delay
  }
})

redis.on('connect', () => {
  console.log('Redis connected')
})

redis.on('error', (error) => {
  console.error('Redis error:', error)
})

export const get = (key) => redis.get(key)
export const set = (key, value, ttl) => redis.set(key, value, 'EX', ttl)
export const del = (key) => redis.del(key)
export const exists = (key) => redis.exists(key)
""",

    "ElasticsearchConnection": """import { Client } from '@elastic/elasticsearch'

export const esClient = new Client({
  node: process.env.ELASTICSEARCH_URL,
  auth: {
    username: process.env.ELASTICSEARCH_USER,
    password: process.env.ELASTICSEARCH_PASSWORD
  }
})

export const createIndex = async (indexName, mappings) => {
  try {
    await esClient.indices.create({
      index: indexName,
      body: { mappings }
    })
  } catch (error) {
    if (error.meta?.body?.error?.type !== 'resource_already_exists_exception') {
      throw error
    }
  }
}

export const search = async (indexName, query) => {
  const { body } = await esClient.search({
    index: indexName,
    body: query
  })
  return body.hits.hits
}
""",

    "FirebaseConnection": """import admin from 'firebase-admin'
import serviceAccount from './firebase-service-account.json'

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: process.env.FIREBASE_DATABASE_URL
})

export const db = admin.firestore()
export const auth = admin.auth()
export const storage = admin.storage()

export const getDocument = async (collection, docId) => {
  const doc = await db.collection(collection).doc(docId).get()
  return doc.exists ? doc.data() : null
}

export const setDocument = async (collection, docId, data) => {
  await db.collection(collection).doc(docId).set(data)
}
""",

    "DynamoDBConnection": """import { DynamoDBClient } from '@aws-sdk/client-dynamodb'
import { DynamoDBDocumentClient, GetCommand, PutCommand } from '@aws-sdk/lib-dynamodb'

const client = new DynamoDBClient({
  region: process.env.AWS_REGION,
  credentials: {
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY
  }
})

export const docClient = DynamoDBDocumentClient.from(client)

export const getItem = async (tableName, key) => {
  const command = new GetCommand({
    TableName: tableName,
    Key: key
  })
  const response = await docClient.send(command)
  return response.Item
}

export const putItem = async (tableName, item) => {
  const command = new PutCommand({
    TableName: tableName,
    Item: item
  })
  await docClient.send(command)
}
""",

    "SQLiteConnection": """import sqlite3 from 'sqlite3'
import { open } from 'sqlite'

export const openDB = async () => {
  return open({
    filename: process.env.SQLITE_DB_PATH || './database.db',
    driver: sqlite3.Database
  })
}

export const db = await openDB()

export const query = async (sql, params = []) => {
  return await db.all(sql, params)
}

export const run = async (sql, params = []) => {
  return await db.run(sql, params)
}

export const get = async (sql, params = []) => {
  return await db.get(sql, params)
}
""",

    "PrismaConnection": """import { PrismaClient } from '@prisma/client'

export const prisma = new PrismaClient({
  log: process.env.NODE_ENV === 'development' ? ['query', 'error', 'warn'] : ['error'],
})

process.on('beforeExit', async () => {
  await prisma.$disconnect()
})

export default prisma
""",

    "MongooseConnectionPooling": """import mongoose from 'mongoose'

const createConnection = (uri, options = {}) => {
  const connection = mongoose.createConnection(uri, {
    ...options,
    maxPoolSize: 10,
    minPoolSize: 2,
    serverSelectionTimeoutMS: 5000,
    socketTimeoutMS: 45000,
  })

  connection.on('connected', () => {
    console.log(`Connection established: ${connection.name}`)
  })

  connection.on('error', (error) => {
    console.error(`Connection error (${connection.name}):`, error)
  })

  return connection
}

export const primaryDB = createConnection(process.env.MONGODB_PRIMARY_URI, {
  readPreference: 'primary'
})

export const replicaDB = createConnection(process.env.MONGODB_REPLICA_URI, {
  readPreference: 'secondaryPreferred'
})

export default { primary: primaryDB, replica: replicaDB }
"""
}

# Write all database templates
total_count = 0

for name, code in schemas.items():
    write_template("schemas", name, code)
    total_count += 1
print(f"✓ Generated {len(schemas)} schema templates")

for name, code in migrations.items():
    write_template("migrations", name, code)
    total_count += 1
print(f"✓ Generated {len(migrations)} migration templates")

for name, code in connections.items():
    write_template("connections", name, code)
    total_count += 1
print(f"✓ Generated {len(connections)} connection templates")

print(f"\n✅ Total database templates generated: {total_count}")
