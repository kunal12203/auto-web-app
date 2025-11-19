import mongoose from 'mongoose'

const cartSchema = new mongoose.Schema({
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User'
  },
  sessionId: String,
  items: [{
    product: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'Product'
    },
    quantity: {
      type: Number,
      min: 1,
      default: 1
    },
    price: Number
  }],
  total: Number,
  expiresAt: {
    type: Date,
    default: () => new Date(+new Date() + 7*24*60*60*1000)
  }
}, {
  timestamps: true
})

export const Cart = mongoose.model('Cart', cartSchema)
