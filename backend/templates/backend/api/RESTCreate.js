// POST create new resource
export const create = async (req, res) => {
  try {
    const resource = new Model(req.body)
    const savedResource = await resource.save()

    res.status(201).json(savedResource)
  } catch (error) {
    res.status(400).json({ message: error.message })
  }
}