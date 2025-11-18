import mongoose from 'mongoose'

const roleSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    unique: true
  },
  permissions: [{
    resource: String,
    actions: [String]
  }],
  description: String
}, {
  timestamps: true
})

export const Role = mongoose.model('Role', roleSchema)
