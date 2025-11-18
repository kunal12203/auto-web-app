export const up = async (db) => {
  const categories = [
    { name: 'Technology', slug: 'technology' },
    { name: 'Business', slug: 'business' },
    { name: 'Lifestyle', slug: 'lifestyle' }
  ]

  await db.collection('categories').insertMany(categories)
}

export const down = async (db) => {
  await db.collection('categories').deleteMany({
    slug: { $in: ['technology', 'business', 'lifestyle'] }
  })
}
