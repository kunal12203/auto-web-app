// Bulk update resources
export const bulkUpdate = async (req, res) => {
  try {
    const { ids, updates } = req.body

    const result = await Model.updateMany(
      { _id: { $in: ids } },
      updates
    )

    res.json({
      matched: result.matchedCount,
      modified: result.modifiedCount
    })
  } catch (error) {
    res.status(400).json({ message: error.message })
  }
}