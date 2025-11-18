// Schema Stitching
import { stitchSchemas } from '@graphql-tools/stitch'

export const stitchedSchema = stitchSchemas({
  subschemas: [
    {
      schema: userSchema,
      executor: userExecutor
    },
    {
      schema: productSchema,
      executor: productExecutor
    }
  ]
})