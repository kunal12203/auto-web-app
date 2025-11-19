/**
 * ErrorFormatter
 * Error response formatter
 */

export const errorformatter = async (req, res, next) => {
  try {
    // Implementation for ErrorFormatter
    // Error response formatter

    // Example logic
    const result = await processLogic(req)

    res.json({
      success: true,
      data: result
    })
  } catch (error) {
    next(error)
  }
}

export default errorformatter
