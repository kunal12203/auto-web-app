import mongoose from 'mongoose'

const productSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  slug: {
    type: String,
    required: true,
    unique: true
  },
  description: String,
  price: {
    type: Number,
    required: true,
    min: 0
  },
  compareAtPrice: Number,
  category: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Category'
  },
  images: [String],
  inventory: {
    quantity: {
      type: Number,
      default: 0
    },
    trackInventory: {
      type: Boolean,
      default: true
    }
  },
  isPublished: {
    type: Boolean,
    default: false
  },
  publishedAt: Date
}, {
  timestamps: true
})

productSchema.index({ name: 'text', description: 'text' })

export const Product = mongoose.model('Product', productSchema)
