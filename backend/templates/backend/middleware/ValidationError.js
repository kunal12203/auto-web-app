/**
 * ValidationError
 * Validation error handler
 */

export const validationerror = async (req, res, next) => {
  try {
    // Implementation for ValidationError
    // Validation error handler

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

export default validationerror
