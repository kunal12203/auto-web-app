export const up = async (db) => {
  await db.collection('users').updateMany(
    {},
    {
      $set: {
        isActive: true
      }
    }
  )
}

export const down = async (db) => {
  await db.collection('users').updateMany(
    {},
    {
      $unset: {
        isActive: ''
      }
    }
  )
}
