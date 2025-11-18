export const up = async (db) => {
  const users = await db.collection('users').find({}).toArray()

  for (const user of users) {
    await db.collection('users').updateOne(
      { _id: user._id },
      {
        $set: {
          age: parseInt(user.age)
        }
      }
    )
  }
}

export const down = async (db) => {
  const users = await db.collection('users').find({}).toArray()

  for (const user of users) {
    await db.collection('users').updateOne(
      { _id: user._id },
      {
        $set: {
          age: String(user.age)
        }
      }
    )
  }
}
