// Soft delete resource
export const softDelete = async (req, res) => {
  try {
    const resource = await Model.findByIdAndUpdate(
      req.params.id,
      { deletedAt: new Date(), isDeleted: true },
      { new: true }
    )

    if (!resource) {
      return res.status(404).json({ message: 'Resource not found' })
    }

    res.json({ message: 'Resource soft deleted' })
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}