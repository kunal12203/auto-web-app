// Export data to CSV
export const exportCSV = async (req, res) => {
  try {
    const resources = await Model.find()

    const csv = resources.map(r => Object.values(r.toObject()).join(',')).join('\n')
    const header = Object.keys(resources[0].toObject()).join(',')

    res.setHeader('Content-Type', 'text/csv')
    res.setHeader('Content-Disposition', 'attachment; filename=export.csv')
    res.send(header + '\n' + csv)
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}