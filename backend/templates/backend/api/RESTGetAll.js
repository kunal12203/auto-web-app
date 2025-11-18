// GET all resources
export const getAll = async (req, res) => {
  try {
    const { page = 1, limit = 10, sort = 'createdAt', order = 'desc' } = req.query

    const resources = await Model.find()
      .sort({ [sort]: order === 'desc' ? -1 : 1 })
      .limit(limit * 1)
      .skip((page - 1) * limit)
      .exec()

    const count = await Model.countDocuments()

    res.json({
      resources,
      totalPages: Math.ceil(count / limit),
      currentPage: page,
      total: count
    })
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}