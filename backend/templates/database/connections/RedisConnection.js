import Redis from 'ioredis'

export const redis = new Redis({
  host: process.env.REDIS_HOST,
  port: process.env.REDIS_PORT,
  password: process.env.REDIS_PASSWORD,
  retryStrategy(times) {
    const delay = Math.min(times * 50, 2000)
    return delay
  }
})

redis.on('connect', () => {
  console.log('Redis connected')
})

redis.on('error', (error) => {
  console.error('Redis error:', error)
})

export const get = (key) => redis.get(key)
export const set = (key, value, ttl) => redis.set(key, value, 'EX', ttl)
export const del = (key) => redis.del(key)
export const exists = (key) => redis.exists(key)
