// Custom GraphQL Directive
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
}