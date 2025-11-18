export const up = async (db) => {
  await db.collection('users').updateMany(
    {},
    {
      $rename: {
        'name': 'fullName'
      }
    }
  )
}

export const down = async (db) => {
  await db.collection('users').updateMany(
    {},
    {
      $rename: {
        'fullName': 'name'
      }
    }
  )
}
