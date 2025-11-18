import mysql from 'mysql2/promise'

const poolConfig = {
  host: process.env.MYSQL_HOST,
  user: process.env.MYSQL_USER,
  password: process.env.MYSQL_PASSWORD,
  database: process.env.MYSQL_DB,
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
}

export const pool = mysql.createPool(poolConfig)

export const query = async (sql, params) => {
  const [rows] = await pool.execute(sql, params)
  return rows
}

export const transaction = async (callback) => {
  const connection = await pool.getConnection()
  await connection.beginTransaction()

  try {
    await callback(connection)
    await connection.commit()
  } catch (error) {
    await connection.rollback()
    throw error
  } finally {
    connection.release()
  }
}
