// Import data from CSV
export const importCSV = async (req, res) => {
  try {
    const file = req.file
    const data = parseCSV(file.buffer)

    const resources = await Model.insertMany(data)

    res.json({
      imported: resources.length,
      resources
    })
  } catch (error) {
    res.status(400).json({ message: error.message })
  }
}