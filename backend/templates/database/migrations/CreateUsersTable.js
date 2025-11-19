export const up = async (db) => {
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
