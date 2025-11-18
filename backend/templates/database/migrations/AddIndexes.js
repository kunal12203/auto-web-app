export const up = async (db) => {
  await db.collection('posts').createIndex({ slug: 1 }, { unique: true })
  await db.collection('posts').createIndex({ author: 1 })
  await db.collection('posts').createIndex({ publishedAt: -1 })
  await db.collection('posts').createIndex(
    { title: 'text', content: 'text' },
    { weights: { title: 10, content: 5 } }
  )
}

export const down = async (db) => {
  await db.collection('posts').dropIndex('slug_1')
  await db.collection('posts').dropIndex('author_1')
  await db.collection('posts').dropIndex('publishedAt_-1')
  await db.collection('posts').dropIndex('title_text_content_text')
}
