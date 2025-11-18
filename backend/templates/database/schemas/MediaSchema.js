import mongoose from 'mongoose'

const mediaSchema = new mongoose.Schema({
  filename: {
    type: String,
    required: true
  },
  originalName: String,
  mimeType: String,
  size: Number,
  url: {
    type: String,
    required: true
  },
  thumbnailUrl: String,
  uploadedBy: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User'
  },
  folder: String,
  tags: [String],
  metadata: mongoose.Schema.Types.Mixed
}, {
  timestamps: true
})

export const Media = mongoose.model('Media', mediaSchema)
