// Apollo Federation
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
])