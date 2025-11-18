import sqlite3 from 'sqlite3'
import { open } from 'sqlite'

export const openDB = async () => {
  return open({
    filename: process.env.SQLITE_DB_PATH || './database.db',
    driver: sqlite3.Database
  })
}

export const db = await openDB()

export const query = async (sql, params = []) => {
  return await db.all(sql, params)
}

export const run = async (sql, params = []) => {
  return await db.run(sql, params)
}

export const get = async (sql, params = []) => {
  return await db.get(sql, params)
}
