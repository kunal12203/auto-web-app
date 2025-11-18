// DELETE resource
export const deleteResource = async (req, res) => {
  try {
    const resource = await Model.findByIdAndDelete(req.params.id)

    if (!resource) {
      return res.status(404).json({ message: 'Resource not found' })
    }

    res.json({ message: 'Resource deleted successfully' })
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}