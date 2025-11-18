export const up = async (db) => {
  // Add foreign key constraint (MongoDB doesn't enforce, this is for documentation)
  await db.collection('posts').createIndex({ author: 1 })
  await db.collection('comments').createIndex({ post: 1 })
}

export const down = async (db) => {
  await db.collection('posts').dropIndex('author_1')
  await db.collection('comments').dropIndex('post_1')
}
