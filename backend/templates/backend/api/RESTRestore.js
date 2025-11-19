// Restore soft deleted resource
export const restore = async (req, res) => {
  try {
    const resource = await Model.findByIdAndUpdate(
      req.params.id,
      { deletedAt: null, isDeleted: false },
      { new: true }
    )

    if (!resource) {
      return res.status(404).json({ message: 'Resource not found' })
    }

    res.json({ message: 'Resource restored', resource })
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}