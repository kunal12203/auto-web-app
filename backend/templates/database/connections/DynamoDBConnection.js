import { DynamoDBClient } from '@aws-sdk/client-dynamodb'
import { DynamoDBDocumentClient, GetCommand, PutCommand } from '@aws-sdk/lib-dynamodb'

const client = new DynamoDBClient({
  region: process.env.AWS_REGION,
  credentials: {
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY
  }
})

export const docClient = DynamoDBDocumentClient.from(client)

export const getItem = async (tableName, key) => {
  const command = new GetCommand({
    TableName: tableName,
    Key: key
  })
  const response = await docClient.send(command)
  return response.Item
}

export const putItem = async (tableName, item) => {
  const command = new PutCommand({
    TableName: tableName,
    Item: item
  })
  await docClient.send(command)
}
