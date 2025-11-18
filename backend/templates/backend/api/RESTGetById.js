// GET single resource by ID
export const getById = async (req, res) => {
  try {
    const resource = await Model.findById(req.params.id)

    if (!resource) {
      return res.status(404).json({ message: 'Resource not found' })
    }

    res.json(resource)
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}