// GraphQL Query Resolver
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
}