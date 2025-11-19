// PUT/PATCH update resource
export const update = async (req, res) => {
  try {
    const resource = await Model.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true, runValidators: true }
    )

    if (!resource) {
      return res.status(404).json({ message: 'Resource not found' })
    }

    res.json(resource)
  } catch (error) {
    res.status(400).json({ message: error.message })
  }
}