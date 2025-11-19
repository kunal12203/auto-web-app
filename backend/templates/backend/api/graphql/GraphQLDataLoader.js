// DataLoader for N+1 prevention
import DataLoader from 'dataloader'

export const createLoaders = () => {
  return {
    userLoader: new DataLoader(async (ids) => {
      const users = await User.find({ _id: { $in: ids } })
      return ids.map(id => users.find(user => user.id === id))
    }),

    postLoader: new DataLoader(async (ids) => {
      const posts = await Post.find({ _id: { $in: ids } })
      return ids.map(id => posts.find(post => post.id === id))
    })
  }
}