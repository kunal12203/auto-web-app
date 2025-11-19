/**
 * Orm12
 * Backend template for orm
 */

export const orm12 = async (req, res, next) => {
  try {
    // Implementation for Orm12

    const result = await processLogic(req)

    return res.json({
      success: true,
      data: result
    })
  } catch (error) {
    next(error)
  }
}

export default orm12
