import mongoose from 'mongoose'

const categorySchema = new mongoose.Schema({
  name: {
    type: String,
    required: true
  },
  slug: {
    type: String,
    required: true,
    unique: true
  },
  description: String,
  parent: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Category'
  },
  icon: String,
  order: {
    type: Number,
    default: 0
  }
}, {
  timestamps: true
})

export const Category = mongoose.model('Category', categorySchema)
