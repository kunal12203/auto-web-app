// Advanced search
export const search = async (req, res) => {
  try {
    const { q, fields = 'name,description' } = req.query

    const searchFields = fields.split(',')
    const searchQuery = {
      $or: searchFields.map(field => ({
        [field]: { $regex: q, $options: 'i' }
      }))
    }

    const results = await Model.find(searchQuery)

    res.json(results)
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}