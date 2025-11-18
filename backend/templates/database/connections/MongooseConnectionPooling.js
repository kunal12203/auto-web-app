import mongoose from 'mongoose'

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
