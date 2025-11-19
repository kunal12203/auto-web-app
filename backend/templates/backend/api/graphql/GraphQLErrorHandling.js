// GraphQL Error Handling
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
}