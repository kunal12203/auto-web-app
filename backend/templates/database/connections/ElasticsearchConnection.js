import { Client } from '@elastic/elasticsearch'

export const esClient = new Client({
  node: process.env.ELASTICSEARCH_URL,
  auth: {
    username: process.env.ELASTICSEARCH_USER,
    password: process.env.ELASTICSEARCH_PASSWORD
  }
})

export const createIndex = async (indexName, mappings) => {
  try {
    await esClient.indices.create({
      index: indexName,
      body: { mappings }
    })
  } catch (error) {
    if (error.meta?.body?.error?.type !== 'resource_already_exists_exception') {
      throw error
    }
  }
}

export const search = async (indexName, query) => {
  const { body } = await esClient.search({
    index: indexName,
    body: query
  })
  return body.hits.hits
}
