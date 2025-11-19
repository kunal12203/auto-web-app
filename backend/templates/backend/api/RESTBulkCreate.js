// Bulk create resources
export const bulkCreate = async (req, res) => {
  try {
    const resources = await Model.insertMany(req.body, { ordered: false })

    res.status(201).json({
      created: resources.length,
      resources
    })
  } catch (error) {
    res.status(400).json({ message: error.message })
  }
}