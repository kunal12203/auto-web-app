export const up = async (db) => {
  const now = new Date()

  await db.collection('products').updateMany(
    {},
    {
      $set: {
        createdAt: now,
        updatedAt: now
      }
    }
  )
}

export const down = async (db) => {
  await db.collection('products').updateMany(
    {},
    {
      $unset: {
        createdAt: '',
        updatedAt: ''
      }
    }
  )
}
