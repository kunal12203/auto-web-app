// GraphQL Subscription
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
}