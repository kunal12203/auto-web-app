import mongoose from 'mongoose'

const webhookEventSchema = new mongoose.Schema({
  type: {
    type: String,
    required: true
  },
  payload: {
    type: mongoose.Schema.Types.Mixed,
    required: true
  },
  source: String,
  processed: {
    type: Boolean,
    default: false
  },
  processedAt: Date,
  attempts: {
    type: Number,
    default: 0
  },
  lastError: String
}, {
  timestamps: true
})

export const WebhookEvent = mongoose.model('WebhookEvent', webhookEventSchema)
