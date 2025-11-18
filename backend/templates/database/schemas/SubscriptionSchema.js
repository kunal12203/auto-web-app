import mongoose from 'mongoose'

const subscriptionSchema = new mongoose.Schema({
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  plan: {
    type: String,
    required: true
  },
  status: {
    type: String,
    enum: ['active', 'cancelled', 'expired', 'past_due'],
    default: 'active'
  },
  startDate: {
    type: Date,
    required: true
  },
  endDate: Date,
  renewalDate: Date,
  paymentMethod: String,
  amount: Number
}, {
  timestamps: true
})

export const Subscription = mongoose.model('Subscription', subscriptionSchema)
