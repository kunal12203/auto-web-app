/**
 * Pubsub13
 * Backend template for pubsub
 */

export const pubsub13 = async (req, res, next) => {
  try {
    // Implementation for Pubsub13

    const result = await processLogic(req)

    return res.json({
      success: true,
      data: result
    })
  } catch (error) {
    next(error)
  }
}

export default pubsub13
