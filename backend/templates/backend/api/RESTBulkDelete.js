// Bulk delete resources
export const bulkDelete = async (req, res) => {
  try {
    const { ids } = req.body

    const result = await Model.deleteMany({ _id: { $in: ids } })

    res.json({
      deleted: result.deletedCount
    })
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}