/**
 * Pubsub14
 * Backend template for pubsub
 */

export const pubsub14 = async (req, res, next) => {
  try {
    // Implementation for Pubsub14

    const result = await processLogic(req)

    return res.json({
      success: true,
      data: result
    })
  } catch (error) {
    next(error)
  }
}

export default pubsub14
