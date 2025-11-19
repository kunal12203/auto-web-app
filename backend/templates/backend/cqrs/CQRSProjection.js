/**
 * CQRSProjection
 */
export const cqrsprojection = async (req, res, next) => {
  try {
    const result = await processLogic(req)
    return res.json({ success: true, data: result })
  } catch (error) {
    next(error)
  }
}

export default cqrsprojection
