// Pagination helper
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
}