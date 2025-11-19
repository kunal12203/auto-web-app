// GraphQL Mutation Resolver
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
}